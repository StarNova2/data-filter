from interface import *
import time

def main():
    data = []
    undo_list = []
    current_data = []

    while True:
        print()
        print(f"\n{bcolors.BOLD}{bcolors.YELLOW}========= MENU ========={bcolors.ENDC}")
        print("1. Load data")
        if data != []:
            print("2. Show number of rows")
            print("3. Show all rows")
            print("4. Stats")
            print(f"{bcolors.BOLD}5. Modify data{bcolors.ENDC}")
            print("6. Undo changes")
            print("7. Save data")
        print("8. Quit")
        print(f"{bcolors.BOLD}{bcolors.YELLOW}========================{bcolors.ENDC}")

        choice = input("\nYour choice : ")

        if choice == "1":
            undo_list = []
            data = load_data()
            undo_list.append(data)
            current_data = undo_list[-1]

        if current_data != []:
            current_data = undo_list[-1]
            if choice == "2":
                print("Current rows:", len(current_data))
                time.sleep(0.5)
            elif choice == "3":
                show_all_rows(current_data)
                input("\nDone watching ?")
            elif choice == "4":
                print("\n")
                stats(current_data)
            elif choice == "5":
                undo_list.append(modif_data(current_data))
            elif choice == "6":
                if len(undo_list)>1:
                    undo_list.pop()
                    current_data = undo_list[-1]
                    print("Changes are undone")
                else:
                    print("Nothing to undo yet")
            elif choice == "7":
                save_data(current_data)
                time.sleep(1)
        if choice == "8":
            print("See you next time.")
            break
        elif choice == "69":
            print("Nice")
            time.sleep(2)
            break
        if choice not in ["1","2","3","4","5","6","7","8","69"]:
            print("Invalid choice.")
            time.sleep(0.5)


if __name__ == "__main__":
    main()
