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
        return f"{self.pid},{self.name},{self.category},{self.brand},{self.quantity},{self.price}"

class PerishableProduct(Product):
    def __init__(self, pid, name, category, brand, quantity, price, expiry):
        super().__init__(pid, name, category, brand, quantity, price)
        self.expiry = expiry
    
    def display_info(self):
        return super().display_info() + f",{self.expiry}"

inventory_list = []
categories = ["Electronics", "Home", "Office", "Food"]
product_ids = set()

def save_data():
    f = open("inventory_data.txt", "w")
    for p in inventory_list:
        f.write(p.display_info() + "\n")
    f.close()
    print("Data saved.")

def load_data():
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
        print("Data loaded.")

def update_item():
    pid_to_update = int(input("Enter ID to update: > "))
    found = False
    for p in inventory_list:
        if p.pid == pid_to_update:
            new_qty = int(input("Enter new quantity: > "))
            p.quantity = new_qty
            found = True
            print("Updated.")
    if not found: print("ID not found.")

def remove_item():
    pid_to_remove = int(input("Enter ID to remove: > "))
    for i in range(len(inventory_list)):
        if inventory_list[i].pid == pid_to_remove:
            del inventory_list[i]
            print("Removed.")
            return
    print("ID not found.")

def main():
    load_data()
    while True:
        print("\n1. Add Item\n2. View Inventory\n3. Update Item\n4. Remove Item\n5. Exit")
        opt = input("> ")
        if opt == "1": 
            name = input("Name: ")
            cat = input("Category: ")
            brand = input("Brand: ")
            qty = int(input("Qty: "))
            price = float(input("Price: "))
            pid = random.randint(100,999)
            if cat == "Food":
                exp = input("Expiry: ")
                inventory_list.append(PerishableProduct(pid, name, cat, brand, qty, price, exp))
            else:
                inventory_list.append(Product(pid, name, cat, brand, qty, price))
        elif opt == "2":
            for p in inventory_list: print(p.display_info())
        elif opt == "3": update_item()
        elif opt == "4": remove_item()
        elif opt == "5":
            save_data()
            break

if __name__ == "__main__":
    main()