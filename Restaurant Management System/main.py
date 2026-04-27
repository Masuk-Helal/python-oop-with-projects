from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurent import Restaurant
from user import Customer, Admin, Employee

res = Restaurant("Mama Fastfood 2")

def customer_menu():
    name = input("Enter your Name: " )
    email = input("Enter your Email: " )
    phone = input("Enter your Phone: " )
    address = input("Enter your Address: " )
    customer = Customer(name=name, email=email, phone=phone, address=address)


    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add Item to cart")
        print("3. View Card")
        print("4. Exit")


        choice = int(input("Enter your Choite : "))
        if choice == 1:
            customer.view_menu(res)
        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter Item Quantity : "))
            customer.add_to_cart(res, item_name, item_quantity)

        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Envalid Input")
        

def admin_menu():
    name = input("Enter your Name: " )
    email = input("Enter your Email: " )
    phone = input("Enter your Phone: " )
    address = input("Enter your Address: " )
    admin = Admin(name=name, email=email, phone=phone, address=address)


    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. view Items")
        print("5. Delete Item")
        print("6. Exit")


        choice = int(input("Enter your Choite : "))
        if choice == 1:
            item_name = input("Enter item name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item Quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(res, item)
        elif choice == 2:

            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            designation = input("Enter employee designation : ")
            age = input("Enter employee age : ")
            salary = input("Enter employee salary : ")
            address = input("Enter employee address : ")

            admin.add_employee(name,email,phone,address,age,designation,salary)

        elif choice == 3:
            admin.view_employee(res)
        elif choice == 4:
            admin.view_menu(res)
        elif choice == 5:
            item_name = input("Enter item name : ")
            admin.remove_item(res,item_name)
        elif choice == 6:
            break
        else:
            print("Envalid Input")


while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid info")
        

