
print("Welcome to Shoprite Shopping list Manager ")
while True:
    print("\nShopping List Manager")
    print("1. View Shopping List")
    print("2. Add Item to Shopping List")
    print("3. Remove Item from Shopping List")
    print("4. Clear Shopping List")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("Your Shopping List:")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
    elif choice == '2':
        item = input("Enter the item you want to add: ")
        shopping_list.append(item)
        print(f"'{item}' added to your shopping list.")
    elif choice == '3':
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            index = int(input("Enter the index of the item to remove: "))
            if 1 <= index <= len(shopping_list):
                removed_item = shopping_list.pop(index - 1)
                print(f"'{removed_item}' removed from your shopping list.")
            else:
                print("Invalid index.")
    elif choice == '4':
        shopping_list.clear()
        print("Shopping list cleared.")
    elif choice == '5':
        print("Thank you for using the Shoprite Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
