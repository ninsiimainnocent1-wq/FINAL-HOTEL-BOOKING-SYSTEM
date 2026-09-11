def pay_fees(data):
    print("\n--- Fee Payment ---")
    reg_no = input("Reg No: ").strip().upper()
    if reg_no not in data["students"]:
        print("Student not found")
        return
    
    student = data["students"][reg_no]
    print(f"Student: {student['name']} | Balance: {student['fees_balance']}")
    
    try:
        amount = int(input("Amount to pay: ").strip())
    except ValueError:
        print("Invalid amount")
        return

    if amount <= 0:
        print("Amount must be positive")
        return
        
    student["fees_paid"] += amount
    student["fees_balance"] -= amount
    if student["fees_balance"] < 0:
        student["fees_balance"] = 0
        
    print(f"Payment recorded. New balance: {student['fees_balance']}")