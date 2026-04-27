from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Item quantity exceeded')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added")
        else:
            print("Item not found")

    def view_cart(self):
        print("**View Cart**")
        print("Name\tPrice\tQuantity")

        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")

        print(f"Total Price : {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear(  )




class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def delete_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()









# Usage
# restaurant = Restaurant("Mama FastFood")

# item1 = FoodItem("Pizza", 12.43, 10)
# item2 = FoodItem("Burger", 10.43, 30)

# # Add items to restaurant menu (FIXED)
# restaurant.menu.add_menu_item(item1)
# restaurant.menu.add_menu_item(item2)

# restaurant.menu.show_menu()

# customer = Customer("Diganta", 3245454, 'adc@gmail.com', 'Gaibandha')
# customer.view_menu(restaurant)

# item_name = input("Enter item name: ")
# item_quantity = int(input("Enter Item Quantity: "))

# customer.add_to_cart(restaurant, item_name, item_quantity)
# customer.view_cart()