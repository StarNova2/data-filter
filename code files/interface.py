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
    while True:
        print("\n==== MODIFICATION MENU ====")
        print("1. Sort data")
        print("2. Filter data")
        print("3. Get the stats")
        print("4. Back")
        print("===========================")

        choice = input("\nYour choice : ")

        if choice == "1":
            sort_menu(data)
        elif choice == "2":
            filter_menu(data)
            time.sleep(0.5)
        elif choice == "3":
            print("\n")
            stats(data)
        elif choice == "4":
            print("Returning to main menu")
            break
        else:
            print("Invalid choice.")
            time.sleep(0.5)

def sort_menu(data):
    pass

def filter_menu(data):
    pass