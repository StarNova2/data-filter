import csv
import json


def load_csv(file_name):
    data_list = []

    try:
        with open(file_name, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                converted_row = {}
                for key, value in row.items():
                    try:
                        converted_row[key] = int(value)
                    except ValueError:
                        try:
                            converted_row[key] = float(value)
                        except ValueError:
                            converted_row[key] = value
                data_list.append(converted_row)
    except FileNotFoundError:
        print("CSV file not found:", file_name)
    except Exception as error:
        print("Error while reading CSV:", error)

    return data_list


def save_csv(file_name, data_list):
    if not data_list:
        print("No data to save in", file_name)
        return

    field_names = list(data_list[0].keys())

    try:
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for row in data_list:
                writer.writerow(row)
        print("Data saved as CSV in", file_name)
    except Exception as error:
        print("Error while writing CSV:", error)


def load_json(file_name):
    try:
        with open(file_name, encoding="utf-8") as file:
            content = json.load(file)
    except FileNotFoundError:
        print("JSON file not found:", file_name)
        return []
    except json.JSONDecodeError as error:
        print("Invalid JSON:", error)
        return []
    except Exception as error:
        print("Error while reading JSON:", error)
        return []

    if isinstance(content, list):
        return content
    else:
        print("JSON file should contain a list.")
        return []


def save_json(file_name, data_list):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data_list, file, indent=2, ensure_ascii=False)
        print("Data saved as JSON in", file_name)
    except Exception as error:
        print("Error while writing JSON:", error)
