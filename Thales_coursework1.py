import random

inventory = {}
categories = ["Electronics", "Home", "Office"]
product_ids = set()


def add_item():
    print("\n--- Add New Item ---")
    name = input("Enter product name: > ")
    
    print("Categories:", categories)
    cat = input("Enter category: > ")
    if cat not in categories:
        print("Category not found, setting to General")
        cat = "General"
        
    brand_name = input("Enter brand name: > ")
    
    brand_info = (brand_name) 
    
    qty = int(input("Enter quantity: > "))
    price = float(input("Enter price: > "))
    
    pid = random.randint(100, 999)
    while pid in product_ids:
        pid = random.randint(100, 999)
    
    product_ids.add(pid)
    
    inventory[pid] = {
        "name": name,
        "category": cat,
        "brand": brand_info,
        "quantity": qty,
        "price": price
    }
    print("Item added successfully!")

def view_inventory():
    print("\nCurrent Inventory:")
    print("--------------------")
    for pid, details in inventory.items():
        print(f"ID: {pid} | Name: {details['name']} | Price: ${details['price']}")
        print(f"Category: {details['category']} | Qty: {details['quantity']}")
        print("")

while True:
    print("\nWelcome to the Inventory Management System!")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")
    
    option = input("Select an option: > ")

    if option == "1":
        add_item()
    elif option == "2":
        view_inventory()
    elif option == "3":
        print("-")
    elif option == "4":
        print("-")
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")