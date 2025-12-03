from interface import *
import time

def main():
    data = []

    while True:
        print()
        print(f"\n{bcolors.BOLD}{bcolors.YELLOW}========= MENU ========={bcolors.ENDC}")
        print("1. Load data")
        if data != []:
            print("2. Show number of rows")
            print("3. Show all rows")
            print("4. Stats")
            print("5. Modify data")
            print("6. Save data")
        print("7. Quit")
        print(f"{bcolors.BOLD}{bcolors.YELLOW}========================{bcolors.ENDC}")

        choice = input("\nYour choice : ")

        if choice == "1":
            data = load_data()
        if data != []:
            if choice == "2":
                print("Current rows:", len(data))
                time.sleep(0.5)
            elif choice == "3":
                show_all_rows(data)
                input("\nDone watching ?")
            elif choice == "4":
                print("\n")
                stats(data)
            elif choice == "5":
                modif_data(data)
            elif choice == "6":
                save_data(data)
                time.sleep(1)
        if choice == "7":
            print("See you next time~~.")
            break
        elif choice == "69":
            print("Nice")
            time.sleep(2)
            break
        else:
            print("Invalid choice.")
            time.sleep(0.5)


if __name__ == "__main__":
    main()
