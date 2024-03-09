from functions import greetings, view_shopping_list, add_item, remove_item, clear_list
print("Welcome to Shoprite Shopping list Manager ")
while True:
    greetings()

    choice = input("Enter your choice: ")
    if choice == '1':
        view_shopping_list()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        clear_list()
    elif choice == '5':
        print("Thank you for using the Shoprite Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
