from save_load import load_csv, save_csv, load_json, save_json

def add_path(file_name):
    if "/" not in file_name and "\\" not in file_name:
        file_name = "data/" + file_name
    return file_name

def load_data():
    print("=== LOAD DATA ===")
    file_name = input("File name (ex: name.csv or name.json) : ")
    file_type = input("File type (csv/json) : ").strip().lower()

    file_name = add_path(file_name)

    if file_type == "csv":
        data = load_csv(file_name)
    elif file_type == "json":
        data = load_json(file_name)
    else:
        print("Unknown type.")
        return []

    print("Loaded", len(data), "rows.")
    if data:
        print("First row:", data[0])
    return data

def save_data(data):
    print("=== SAVE DATA ===")
    file_name = input("Output file name (ex: goty) : ")
    file_type = input("File type (csv/json) : ").strip().lower()

    if file_type == "csv" and not file_name.endswith(".csv"):
        file_name += ".csv"
    if file_type == "json" and not file_name.endswith(".json"):
        file_name += ".json"

    file_name = add_path(file_name)

    if file_type == "csv":
        save_csv(file_name, data)
    elif file_type == "json":
        save_json(file_name, data)
    else:
        print("What is that ? The only existing types in the universe are csv and json.")

def show_all_rows(data):
    print("=== ALL ROWS ===")
    if not data:
        print("No data to show.")
        return
    
    for index, row in enumerate(data, start=1):
        print(f"Row {index}: {row}")

def main():
    data = []

    while True:
        print()
        print("==== MENU ====")
        print("1. Load data")
        print("2. Show number of rows")
        print("3. Show all rows")
        print("4. Save data")
        print("5. Quit")

        choice = input("Your choice : ")

        if choice == "1":
            data = load_data()
        elif choice == "2":
            print("Current rows:", len(data))
        elif choice == "3":
            show_all_rows(data)
        elif choice == "4":
            if data:
                save_data(data)
            else:
                print("No data loaded yet.")
        elif choice == "5":
            print("See you next time~~.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
