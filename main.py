from functions import greetings, view_shopping_list, add_item
print("Welcome to Shoprite Shopping list Manager ")
while True:
    greetings()

    choice = input("Enter your choice: ")
    if choice == '1':
        view_shopping_list()
    elif choice == '2':
        item = input("Enter the item you want to add: ")
        shopping_list.append(item)
        print(f"'{item}' added to your shopping list.")
    elif choice == '3':
        add_item()
    elif choice == '4':
        shopping_list.clear()
        print("Shopping list cleared.")
    elif choice == '5':
        print("Thank you for using the Shoprite Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
