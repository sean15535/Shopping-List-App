shopping_list = []
print("Welcome to Shoprite Shopping list Manager ")
while True:
    print("1. Display Shopping  List\n2. Add item to cart \n3. Mark item as Bought\n4. Remove Item\n5. Exit")
    choice = int(input(">>> "))
    if choice == 1:
        if not shopping_list:
            print("Your Shopping List is empty")
        else:
            print("Items in your shopping list are: ")
            for  index, items in enumerate (shopping_list, start=1):
                print(f"{index} - {items} ")
    elif choice == 2:
            print("Enter item to add to your cart: ")
            response = input(">>>  ")
            shopping_list.append(response)
            print(f" {response} has been added to your shopping list successfully")
    elif choice == 3:
         if not shopping_list:
              print("Your Shopping List is empty")
         else:
            for  index, items in enumerate (shopping_list, start=1):
                print(f"{index} - {items} ")
            reply = int(input("Enter item number  that you have brought from your shopping list: "))
            if 1 <= reply <= len(shopping_list):
                 bought_item = shopping_list.pop(reply)
                 print(f"item {bought_item} has been bought")
            else:
                print(" Item not found")
    elif choice == 4:
         for  index, items in enumerate (shopping_list, start=1):
          print(f"{index} - {items} ")
         response = input("Enter item to be removed from the Shopping list: ")
         if 1 <= reply <= len(shopping_list):
            removed_item = shopping_list.remove(response)
            print(f"Item {removed_item} has been removed from the shopping list")
         else:
             print("Item not found")
             
    elif choice == 5 :
         print(" Closing Shoprite Shopping List Manager App")
         break
    else:
        print("invalid Command")     
else:
    print("Invalid Command")
     


            

