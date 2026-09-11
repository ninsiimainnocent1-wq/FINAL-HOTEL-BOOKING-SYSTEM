from file_manager import load_data, save_data
from students import register_student
from fees import pay_fees
from reports import search_student, occupancy_report, defaulters_report

def main():
    data = load_data()
    while True:
        print("\n===== Hostel Management System =====")
        print("1. Register / Allocate Student")
        print("2. Fee Payment")
        print("3. Search Student")
        print("4. Hostel Occupancy Report")
        print("5. Fee Defaulters Report")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            register_student(data)
            save_data(data)
        elif choice == '2':
            pay_fees(data)
            save_data(data)
        elif choice == '3':
            search_student(data)
        elif choice == '4':
            occupancy_report(data)
            input("Press Enter...")
        elif choice == '5':
            defaulters_report(data)
            input("Press Enter to continue...")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
            input("Press Enter...")

if __name__ == "__main__":
    main()