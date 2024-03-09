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
        return "Your shopping list is empty."
    print("Your Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
def add_item():
    if not shopping_list:
        return "Your shopping list is empty."
    index = int(input("Enter the index of the item to remove: "))
    if 1 <= index <= len(shopping_list):
        removed_item = shopping_list.pop(index - 1)
        return f"'{removed_item}' removed from your shopping list."
    else:
        print("Invalid index.")
