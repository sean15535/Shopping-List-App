shopping_list = []

def greetings():
    print("\nShopping List Manager")
    print("1. View Shopping List")
    print("2. Add Item to Shopping List")
    print("3. Remove Item from Shopping List")
    print("4. Clear Shopping List")
    print("5. Exit")

def view_shopping_list():
    if not shopping_list:
        print("Your shopping list is empty.")
        return
    print("Your Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")

def remove_item():
    if not shopping_list:
        return "Your shopping list is empty."
    index = int(input("Enter the index of the item to remove: "))
    try:
        if 1 <= index <= len(shopping_list):
            removed_item = shopping_list.pop(index - 1)
            print(f"'{removed_item}' removed from your shopping list.")
    except ValueError:
        print("Invalid index.")

def add_item():
        item = input("Enter the item you want to add: ")
        shopping_list.append(item)
        return f"'{item}' added to your shopping list."

def clear_list():
    shopping_list.clear()
    print("Shopping list cleared.")