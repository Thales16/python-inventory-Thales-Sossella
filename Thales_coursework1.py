inventory = {}

categories = ["Electronics", "Home", "Office"]

product_ids = set()
product_ids.add(101) 

inventory[101] = {
    "name": "Laptop",
    "category": "Electronics",
    "brand": ("Dell", "USA"), 
    "quantity": 5,
    "price": 799.99
}

print("Data structures initialized.")
print("Categories available:", categories)