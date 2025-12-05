from save_load import *
from sort import *
from stats import *
from filter import *
import time

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def add_path(file_name):
    if "/" not in file_name and "\\" not in file_name:
        file_name = "data/" + file_name
    return file_name

def load_data():
    print("\n=== LOAD DATA ===")
    file_name = input("File name (ex: name.csv or name.json) : ")
    file_name_splitted = file_name.split(".")
    file_type = file_name_splitted[-1]

    file_name = add_path(file_name)

    if file_type == "csv":
        data = load_csv(file_name)
    elif file_type == "json":
        data = load_json(file_name)
    else:
        print("Unsupported or unknown type.")
        return []

    print("Loaded", len(data), "rows.")
    if data:
        print("First row:", data[0])
    return data

def save_data(data):
    print("\n=== SAVE DATA ===")
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
    print("\n=== ALL ROWS ===")
    if not data:
        print("No data to show.")
        return
    
    for index, row in enumerate(data, start=1):
        print(f"Row {index}: {row}")



def modif_data(data):
    modified_data = data
    while True:
        print("\n==== MODIFICATION MENU ====")
        print("1. Sort data")
        print("2. Filter data")
        print("3. Get the stats")
        print("4. Back")
        print("===========================")

        choice = input("\nYour choice : ")

        if choice == "1":
            modified_data = sort_menu(modified_data)
            print("\nData sorted.")
            time.sleep(1)
        elif choice == "2":
            modified_data = filter_menu(modified_data)
            print("\nData filtered.")
            time.sleep(1)
        elif choice == "3":
            print("\n")
            stats(modified_data)
        elif choice == "4":
            print("Returning to main menu")
            return modified_data
        else:
            print("Invalid choice.")
            time.sleep(0.5)

def sort_menu(data):
    while True:
        sort_index = 1
        print("\nRows you can sort data by :")
        for i in data[0].keys():
            print(f"{sort_index}. {i}")
            sort_index +=1
        index_input = input("\nWhat row to use for sorting ?\n")

        try:
            index_input = int(index_input)-1
            if index_input >= 0 and index_input < len(data[0]):
                while True:
                    sort_key = input("\nIn what order will the data be sorted ? (0 for ascending, 1 for descending)\n")

                    try:
                        sort_key = int(sort_key)
                        if sort_key == 0 or sort_key == 1:
                            return sort_function(data,index_input,sort_key)       
                                             
                        else:
                            print("\nIncorrect choice")

                    except ValueError:
                        print("\nIncorrect choice")

            else:
                print("\nIncorrect index")

        except ValueError:
            print("\nIncorrect choice")

def filter_menu(data):
    # 1 data 2 index 3 criteria 4 comparison
    while True:
        sort_index = 1
        print("\nRows you can filter data by :")
        for i in data[0].keys():
            print(f"{sort_index}. {i}")
            sort_index +=1
        index_input = input("\nWhat row to use for filtering ?\n")

        try:
            index_input = int(index_input)-1
            if index_input >= 0 and index_input < len(data[0]):
                while True:
                    criteria = input("\nWhat is the criteria you will be filtering the data by ? (int)\n")

                    try:
                        criteria = int(criteria)
                        while True:
                            comparison = input("\nBy what way the data will be sorted ? (1 for data under the criteria, 2 for data over the criteria, 3 for data equals to the criteria\n")

                            try:
                                comparison = int(comparison)
                                if comparison == 1 or comparison == 2 or comparison == 3:
                                    return filter(data,index_input,criteria,comparison)       
                                                        
                                else:
                                    print("\nIncorrect choice")

                            except ValueError:
                                print("\nIncorrect choice")
                    except ValueError:
                        print("\nIncorrect input")

            else:
                print("\nIncorrect index")

        except ValueError:
            print("\nIncorrect choice")