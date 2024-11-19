shopping_list = {}

def add_items():
    item_name = input('Please Enter Item Name - ')
    item_quantity = input('Please Enter Required Quantity - ')
    if item_name not in shopping_list:
        shopping_list[item_name] = item_quantity
    else:
        print('Existing Item! You can update the Quantity!')
        update_choice = input('Do you want to update the quantity? Enter y/n')
        if update_choice == 'y':
            updated_quantity = input('Please enter the updated quantity - ')
            if updated_quantity != 0:
                shopping_list[item_name] = updated_quantity

def show_items():
    for item in shopping_list.items():
        print(item)

def delete_item():
    show_items()
    item = input('Please enter the item name to be deleted - ')
    shopping_list.pop(item)

def help():
    print('--Help Menu--')
    print('Press 1 to Add Items ')
    print('Press 2 to Delete an Item ')
    print('Press 3 to Show the added Items ')
    print('Press 4 to Exit the App ')
     
print('!!---- Welcome to Foodie ----!!')
choice = 0
while choice != 4:
    if choice == 1:
        add_items()
    elif choice == 2:
        delete_item()
    elif choice == 3:
        show_items()
    help()
    choice = int(input('Please enter your choice - '))

