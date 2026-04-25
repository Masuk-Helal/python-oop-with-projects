

from abc import ABC

class User():
    def __init__(self,name,phone,email,address):
        self.name = name 
        self.email = email 
        self.address = address
        self.phone = phone

class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address) 
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address) 
        self.employees = []

    def add_employee(self, name, email, phone, address,age,designation,salary):
        employee = Employee(name,email,phone,address,age,designation,salary)
        self.employees.append(employee)
        print(f"{name} is added!")

    def view_employee(self):
        print(f"Employee List")
        for emp in self.employees:
            print(emp.name, emp.email ,emp.phone, emp.address)

add = Admin("karim", "345435", "karim@gmail.com", "Dhaka")
add.add_employee("Sagor", "s@gmail.com", "3432543", "gaibandha", 45, "chef", 12343)
add.view_employee()

