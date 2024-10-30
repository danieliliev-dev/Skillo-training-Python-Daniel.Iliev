#Problem 0:
#Create a class "Person" with a special method "__str__" to provide a string representation.
#Instantiate an object of this class and print it.
class Person:
    def __init__(self, name, familyname):
        self.firstname = name
        self.lastname = familyname

    def __str__(self):
        return f"Person(first name: {self.firstname}, last name: {self.lastname})"
person = Person("Tosho", "Goshov")
print(person)

#Problem 1:
#Define a class "Email" with special methods "__eq__" and "__ne__" to compare two email addresses.
#Test the equality and inequality operators with different email instances.
class Email:
    def __init__(self, address):
        self.address = address.lower()
    def __eq__(self, other):
        if isinstance(other, Email):
            return self.address == other.address
        return
    def __ne__(self, other):
        if isinstance(other, Email):
            return self.address != other.address
        return
email1 = Email("pencho@poshta.com")
email2 = Email("gencho@poshta.COM")
email3 = Email("dimitrichka@poshta.com")
print(email1 != email2)
print(email1 != email3)
print(email1 == email2)
print(email1 == email3)

#Problem 2:
#Create a class "Student" with protected attributes for name and age.
#Implement property getter and setter methods for these attributes. Demonstrate their usage.
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age cannot be a negative number.")
        self._age = new_age
student = Student("Ganka", 23)
print(f"Name: {student.name}, Age: {student.age}")
student.name = "Boncho"
student.age = 19
print(f"Updated Name: {student.name}, Updated Age: {student.age}")
try:
    student.age = -90
except ValueError as e:
    print(e)

#Problem 3:
#Design a class "BankAccount" with methods for deposit, withdrawal, and balance inquiry.
# Use encapsulation to protect the account balance (it should be read-only).
# Demonstrate proper usage of the class.
class BankAccount:
    def __init__(self, account_owner, starting_balance=0):
        self.account_owner = account_owner
        self._balance = starting_balance
    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print("Deposit amount must be a positive number.")
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self._balance:.2f}")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be a positive number.")

account = BankAccount("Penka", 1000)
print(f"Account owner: {account.account_owner}, Balance: ${account.balance:.2f}")
account.deposit(1500)
account.withdraw(400)
account.withdraw(1900)
print(f"Current balance: ${account.balance:.2f}")

#Problem 4:
#Implement a class "Rectangle" with private attributes for length and width.
# Include special methods "__eq__" and "__lt__" to compare rectangles based on area and perimeter.
# Test the comparison operators with multiple instances.
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    @property
    def area(self):
        return self.__length * self.__width
    @property
    def perimeter(self):
        return 2 * (self.__length + self.__width)
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.perimeter < other.perimeter
        return NotImplemented
rect1 = Rectangle(9, 11)
rect2 = Rectangle(23, 15)
rect3 = Rectangle(42, 5)
print(rect1 < rect2)
print(rect1 < rect3)
print(rect3 < rect1)
print(rect1 == rect2)
print(rect1 == rect3)

#Problem 5:
#Design an abstract class "Vehicle" with a method "start_engine()".
#Create two subclasses, "Car" and "Bicycle," implementing the "start_engine()" method differently.
#Demonstrate polymorphism by calling the method on instances of both subclasses.
class Vehicle:
    def start_engine(self):
        raise NotImplementedError("methods override.")
class Car(Vehicle):
    def start_engine(self):
        return "engine starts"
class Bicycle(Vehicle):
    def start_engine(self):
        return "bicycle's wheels begin to rotate"
def vehicle_start(vehicle: Vehicle):
    print(vehicle.start_engine())
car = Car()
bicycle = Bicycle()
vehicle_start(car)
vehicle_start(bicycle)

#Problem 6:
#Implement a class "Book" with special methods "__str__" and "__len__"
# to provide a string representation and the number of pages. Create instances of "Book"
# and demonstrate the use of these methods.
class Book:
    def __init__(self, booktitle, author, amountofpages):
        self.title = booktitle
        self.author = author
        self.pages = amountofpages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return self.pages
book1 = Book("Pod Igoto", "Ivan Vazov", 1878)
book2 = Book("Iliada", "Omir", 2121)
print(book1)
print(f"Number of pages: {len(book1)}")
print(book2)
print(f"Number of pages: {len(book2)}")