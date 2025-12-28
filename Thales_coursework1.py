inventory = {}
categories = ["Electronics", "Home", "Office"]
product_ids = set()

while True:
    print("\nWelcome to the Inventory Management System!")
    print("===========================================")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")
    
    option = input("Select an option: > ")

    if option == "1":
        print("Add item selected (-)")
    elif option == "2":
        print("View inventory selected (-)")
    elif option == "3":
        print("Update item selected (-)")
    elif option == "4":
        print("Remove item selected (-)")
    elif option == "5":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid option, try again.")