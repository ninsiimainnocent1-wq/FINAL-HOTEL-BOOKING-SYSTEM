def search_student(data):
    reg = input("Enter reg no to search: ").strip().upper()
    s = data.get("students", {}).get(reg)
    if s:
        print(f"\nFound: {reg} - {s.get('name')} - Block {s.get('block')} Room {s.get('room')} - Balance {s.get('fees_balance')}")
    else:
        print("Student not found!")

def occupancy_report(data):
    print("\n--- Occupancy Report ---")
    students = data.get("students", {})
    if not students:
        print("No students found!")
        return
    for reg, s in students.items():
        print(f"{reg} - {s.get('name')} - Block: {s.get('block')} Room: {s.get('room')}")

def defaulters_report(data):
    print("\n--- Fee Defaulters ---")
    students = data.get("students", {})
    found = False
    for reg, s in students.items():
        balance = s.get("fees_balance", 0)
        if balance > 0:
            print(f"{reg} - {s.get('name')} - Balance: {balance} - Room {s.get('block')} {s.get('room')}")
            found = True
    if not found:
        print("No defaulters. All cleared!")