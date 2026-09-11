from hostel import HOSTELS, is_room_valid, get_room_capacity

def register_student(data):
    print("\n--- Register New Student ---")
    reg_no = input("Registration No (e.g. 24/U/1234): ").strip().upper()
    if reg_no in data["students"]:
        print("Student already exists!")
        return

    name = input("Full Name: ").strip()
    course = input("Course: ").strip()
    contact = input("Contact: ").strip()
    
    print("\nAvailable Hostels:")
    for i, block in enumerate(HOSTELS.keys(), 1):
        print(f"{i}. {block}")
    
    block_choice = input("Choose block name (copy exactly): ").strip()
    if block_choice not in HOSTELS:
        print("Invalid block name")
        return
        
    print(f"Rooms in {block_choice}: {', '.join(HOSTELS[block_choice]['rooms'])}")
    room = input("Room No: ").strip().upper()

    if not is_room_valid(block_choice, room):
        print("Invalid room for that block")
        return

    occupied = len(data["rooms"].get(room, []))
    cap = get_room_capacity(block_choice)
    if occupied >= cap:
        print(f"Room {room} is full ({cap}/{cap})")
        return

    data["students"][reg_no] = {
        "name": name,
        "course": course,
        "contact": contact,
        "block": block_choice,
        "room": room,
        "fees_paid": 0,
        "fees_balance": 1500000
    }
    data["rooms"].setdefault(room, []).append(reg_no)
    print(f"Success! {name} allocated to {block_choice}, Room {room}")