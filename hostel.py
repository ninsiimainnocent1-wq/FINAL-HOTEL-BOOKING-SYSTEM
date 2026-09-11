HOSTELS = {
    "Block A - Nsibirwa": {"rooms": ["A01", "A02", "A03", "A04", "A05"], "capacity": 2},
    "Block B - Mary Stuart": {"rooms": ["B01", "B02", "B03", "B04"], "capacity": 3},
    "Block C - Complex": {"rooms": ["C01", "C02", "C03"], "capacity": 2},
    "Block D - Africa": {"rooms": ["D01", "D02"], "capacity": 4}
}

def is_room_valid(block, room):
    return block in HOSTELS and room in HOSTELS[block]["rooms"]

def get_room_capacity(block):
    return HOSTELS.get(block, {}).get("capacity", 2)

def get_occupancy(data):
    print("\n--- Hostel Occupancy ---")
    for block_name, block_info in HOSTELS.items():
        print(f"{block_name} (Capacity per room: {block_info['capacity']})")
        for room in block_info["rooms"]:
            count = len(data["rooms"].get(room, []))
            status = "Full" if count >= block_info["capacity"] else f"{count}/{block_info['capacity']}"
            print(f" {room}: {status}")