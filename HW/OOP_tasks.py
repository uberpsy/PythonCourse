# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Book' to represent a book. The class should have the following attributes and methods:

Attributes:
- 'title': a string representing the title of the book.
- 'author': a string representing the author of the book.
- 'pages': an integer representing the number of pages in the book.

Methods:
- 'get_book_info()': a method that returns a string with the book's title, author, and number of pages.

Create an instance of the 'Book' class with information about a book and demonstrate the usage of the 'get_book_info' method.
"""

# Define the Book class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = int(pages)
    
    def get_book_info(self):
        return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'


# TEST
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 192)
print(book1.get_book_info())

# EXPECTED OUTPUT
# Title: The Great Gatsby, Author: F. Scott Fitzgerald, Pages: 192


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Car' to represent a car. The class should have the following attributes and methods:

Attributes:
- 'make': a string representing the make of the car (e.g., Toyota, Honda).
- 'model': a string representing the model of the car (e.g., Camry, Civic).
- 'year': an integer representing the manufacturing year of the car.

Methods:
- 'start_engine()': a method that prints a message indicating that the car's engine has started.
- 'stop_engine()': a method that prints a message indicating that the car's engine has stopped.

Create an instance of the 'Car' class with information about a car and demonstrate the usage of the 'start_engine' and 'stop_engine' methods.

"""

# Define the Car class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f'Engine started for {self.make} {self.model} {self.year}')
    
    def stop_engine(self):
        print(f'Engine stopped for {self.make} {self.model} {self.year}')

# TEST
car1 = Car("Toyota", "Camry", 2022)
car1.start_engine()
car1.stop_engine()

# EXPECTED OUTPUT:
# Engine started for Toyota Camry 2022
# Engine stopped for Toyota Camry 2022



# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Student' to represent a student. The class should have the following attributes and methods:

Attributes:
- 'name': a string representing the student's name.
- 'student_id': an integer representing the student's ID.
- 'courses': a list representing the courses the student is enrolled in.

Methods:
- 'add_course(course_name)': a method that adds a course to the student's list of courses.
- 'remove_course(course_name)': a method that removes a course from the student's list of courses.
- 'list_courses()': a method that prints the list of courses the student is enrolled in.

Create an instance of the 'Student' class with your own information and demonstrate the usage of the methods.
"""

# Define the Student class

class Student:
    def __init__(self,name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
       

    def add_course(self, course_name):
        self.courses.append(course_name)

    def remove_course(self, course_name):
        self.courses.remove(course_name)

    def list_courses(self):
        print(f'Courses: {", ".join(self.courses)}')
       

# TEST
student1 = Student("Alice", 12345)
student1.add_course("Math")
student1.add_course("History")
student1.list_courses()

#EXPECTED OUTPUT:
# Courses: Math,History


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'BankAccount' to represent a bank account. The class should have the following attributes and methods:

Attributes:
- 'account_number': a string representing the account number.
- '__balance': a float representing the current balance of the account. It must be private

Methods:
- 'deposit(amount)': a method that adds the provided amount to the account balance.
- 'withdraw(amount)': a method that subtracts the provided amount from the account balance.
- 'get_balance()': a method that returns the current balance of the account.

Create an instance of the 'BankAccount' class with your own account information and demonstrate the usage of the methods.
"""

# Define the BankAccount class

class BankAccount:
    def __init__(self, account_number, __balance):
        self.account_number = account_number
        self.__balance = float(__balance)

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
        


# TEST:
account1 = BankAccount("12345", 1000.0)
account1.deposit(500.0)
account1.withdraw(200.0)
print(account1.get_balance())

# # try to access balance directly:
account1.__balance = 0
print(account1.get_balance())

# OUTPUT:
# 1300.0
# 1300.0


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Create a base class called 'Shape' to represent a geometric shape. The class should have the following attributes and methods:

Attributes:
- 'name': a string representing the name of the shape.

Methods:
- 'area()': a method that will return the string 'Not implemented for common shape'

Create two subclasses, 'Rectangle' and 'Circle', that inherit from the 'Shape' class and implement their specific area calculation methods.

Demonstrate the usage of the 'Rectangle' and 'Circle' classes by creating instances of each and calculating their respective areas.
"""

# Define the Shape base class

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print('Not implemented for common shape')

# Define the Rectangle class inheriting from Shape
        
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
# Define the Circle class inheriting from Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return 3.141592653*self.radius**2

# TEST:
rectangle1 = Rectangle("Rectangle", 5.0, 3.0)
circle1 = Circle("Circle", 2.0)
print(rectangle1.area())
print(f'{circle1.area():.5f}')

# EXPECTED OUTPUT:
# 15.0
# 12.56637