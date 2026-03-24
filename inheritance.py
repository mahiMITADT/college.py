# Program: Demonstrating inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_emp(self):
        self.show()
        print("Salary:", self.salary)


p = Employee("Rahul", 25, 30000)
p.show_emp()
