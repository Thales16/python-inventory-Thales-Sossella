import random
import os

class Product:
    def __init__(self, pid, name, category, brand, quantity, price):
        self.pid = pid
        self.name = name
        self.category = category
        self.brand = brand 
        self.quantity = quantity
        self.price = price
    
    def display_info(self):
        return f"ID: {self.pid} | Name: {self.name} | Cat: {self.category} | Brand: {self.brand} | Qty: {self.quantity} | Price: ${self.price}"
    
    def get_save_string(self):
        return f"{self.pid},{self.name},{self.category},{self.brand},{self.quantity},{self.price}"

class PerishableProduct(Product):
    def __init__(self, pid, name, category, brand, quantity, price, expiry):
        super().__init__(pid, name, category, brand, quantity, price)
        self.expiry = expiry
    
    def display_info(self):
        return super().display_info() + f" | Exp: {self.expiry}"
        
    def get_save_string(self):
        return super().get_save_string() + f",{self.expiry}"

inventory_list = []
categories = ["Electronics", "Home", "Office", "Food"]
product_ids = set()

def save_data():
    try:
        f = open("inventory_data.txt", "w")
        for p in inventory_list:
            f.write(p.get_save_string() + "\n")
        f.close()
        print("Saving inventory to file...")
    except Exception as e:
        print("Error saving file:", e)

def load_data():
    try:
        if os.path.exists("inventory_data.txt"):
            f = open("inventory_data.txt", "r")
            for line in f:
                data = line.strip().split(",")
                pid = int(data[0])
                product_ids.add(pid)
                
                if len(data) == 6:
                    p = Product(pid, data[1], data[2], data[3], int(data[4]), float(data[5]))
                    inventory_list.append(p)
                elif len(data) == 7:
                    p = PerishableProduct(pid, data[1], data[2], data[3], int(data[4]), float(data[5]), data[6])
                    inventory_list.append(p)
            f.close()
            print("Inventory loaded from file.")
    except Exception as e:
        print("Error loading file. Starting fresh.")

def add_item():
    try:
        print("\n--- Add New Item ---")
        name = input("Enter product name: > ")
        print(f"Categories: {categories}")
        cat = input("Enter category: > ")
        
        if cat not in categories:
            print("Category not valid! Setting to General.")
            cat = "General"
            
        brand = input("Enter brand name: > ")
        
        qty = int(input("Enter quantity: > "))
        price = float(input("Enter price: > "))
        
        pid = random.randint(100, 999)
        while pid in product_ids:
            pid = random.randint(100, 999)
        product_ids.add(pid)
        
        if cat == "Food":
            expiry = input("Enter expiration date: > ")
            new_prod = PerishableProduct(pid, name, cat, brand, qty, price, expiry)
        else:
            new_prod = Product(pid, name, cat, brand, qty, price)
            
        inventory_list.append(new_prod)
        print("Item added successfully!")
        
    except ValueError:
        print("Error: Please enter valid numbers for quantity and price!")

def view_inventory():
    print("\nCurrent Inventory:")
    print("--------------------")
    if not inventory_list:
        print("Inventory is empty.")
    for p in inventory_list:
        print(p.display_info())

def update_item():
    try:
        pid_search = int(input("Enter product ID to update: > "))
        found = False
        for p in inventory_list:
            if p.pid == pid_search:
                new_qty = int(input("Enter new quantity: > "))
                p.quantity = new_qty
                print("Inventory updated successfully!")
                found = True
                break
        if not found:
            print("ID not found.")
    except ValueError:
        print("Invalid input. ID and Quantity must be numbers.")

def remove_item():
    try:
        pid_search = int(input("Enter ID to remove: > "))
        found = False
        for i in range(len(inventory_list)):
            if inventory_list[i].pid == pid_search:
                del inventory_list[i]
                print("Item removed.")
                found = True
                break
        if not found:
            print("ID not found.")
    except ValueError:
        print("Invalid ID format.")


def main():
    load_data()
    
    while True:
        print("\n===========================================")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Exit")
        
        choice = input("Select an option: > ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            save_data()
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()