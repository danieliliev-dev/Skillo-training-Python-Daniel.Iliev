# Problem 0:
# Complete the following function so that it returns the sum of the elements in the list passed as an argument.
# Call your function several times in order to test it
# def sum_elements(arr):
# result = 0
# insert code here
# return result
def sum_elements(arr):
    result = 0
    for element in arr:
        result += element
    return result
print(sum_elements([5, 15, 25, 35]))
print(sum_elements([100, 200, 300]))
print(sum_elements([-10, 10, -20, 20]))
print(sum_elements([2.5, 3.5, 4.5]))

# Problem 1: Simple Calculator Function
# Define a function called `simple_calculator` that takes two numbers and an operator ('+', '-', '*', or '/')
# as arguments and returns the result of the operation.
def simple_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "division by zero"
    else:
        return "unusable operator"
print(simple_calculator(20, 10, '+'))
print(simple_calculator(20, 10, '-'))
print(simple_calculator(20, 10, '*'))
print(simple_calculator(20, 10, '/'))
print(simple_calculator(15, 0, '/'))
print(simple_calculator(15, 3, '**'))

# Problem 2: Area of Shapes
# Create a module named `geometry` with functions to calculate the area of common shapes like
# a square, rectangle, triangle, and circle. Import this module and use it
# to calculate the areas of different shapes. You should be able to use the function
# for calculating the area of a rectangle to calculate the area of a square by passing in only one argument.
import math
def area_square(side):
    return area_rectangle(side, side)
def area_rectangle(length, width):
    return length * width
def area_triangle(base, height):
    return 0.5 * base * height
def area_circle(radius):
    return math.pi * radius * radius

import geometry
square_side = 9
print(f"area of square: {geometry.area_square(square_side)}")
rectangle_length = 3
rectangle_width = 7
print(f"area of rectangle: {geometry.area_rectangle(rectangle_length, rectangle_width)}")
triangle_base = 5
triangle_height = 3
print(f"The area of the triangle is {geometry.area_triangle(triangle_base, triangle_height)}")
circle_radius = 18
print(f"The area of the circle is {geometry.area_circle(circle_radius)}")

# Problem 3: Temperature Conversion
# Write a program that converts temperatures between Celsius and Fahrenheit.
# Create two functions, one for each conversion, and use them in a program
# to convert temperatures provided by the user. Write another script which tests these functions.
def from_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
def from_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
def tempcalctest():
    while True:
        option = input(
            "Pick one: (C) - from Celsius to Fahrenheit, (F) - from Fahrenheit to Celsius (X) - exit: ").upper()
        if option == 'C':
            celsius = float(input("temperature in Celsius: "))
            print(f"{celsius}°C is {from_celsius_to_fahrenheit(celsius)}°F")
        elif option == 'F':
            fahrenheit = float(input("temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F is {from_fahrenheit_to_celsius(fahrenheit)}°C")
        elif option == 'X':
            print("exiting")
            break
        else:
            print("No valid option picked, try again.")
if __name__ == "__main__":
    tempcalctest()
import temperature_converter
def test_from_celsius_to_fahrenheit():
    assert temperature_converter.from_celsius_to_fahrenheit(0) == 32
    assert temperature_converter.from_celsius_to_fahrenheit(100) == 212
    assert temperature_converter.from_celsius_to_fahrenheit(-40) == -40
    print("test from_celsius_to_fahrenheit is successful")
def test_from_fahrenheit_to_celsius():
    assert temperature_converter.from_fahrenheit_to_celsius(32) == 0
    assert temperature_converter.from_fahrenheit_to_celsius(212) == 100
    assert temperature_converter.from_fahrenheit_to_celsius(-40) == -40
    print("test for from_fahrenheit_to_celsius is successful")
if __name__ == "__main__":
    test_from_celsius_to_fahrenheit()
    test_from_fahrenheit_to_celsius()

# Problem 4: Factorial(again):
# Write a recursive function which computes the Factorial of a given integer.
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial_iterative(5))
print(factorial_iterative(7))

# Problem 5: Online Shopping Cart
# Create a Python program that simulates an online shopping cart using a global dictionary variable.
# Every customer has unique id as a key. Define functions to add items to the cart,
# remove items, calculate the total price, and display the contents of the cart.
# Allow the user to interact with the cart by adding and removing items.

class ShoppingCart:
    def __init__(self):
        self.carts = {}

    def add_item(self, customer_id, item, price):
        if customer_id not in self.carts:
            self.carts[customer_id] = []
        self.carts[customer_id].append((item, price))
        print(f"adding {item} for {price} BGN cart of customer: {customer_id}.")

    def remove_item(self, customer_id, item):
        if customer_id in self.carts:
            for i, (cart_item, price) in enumerate(self.carts[customer_id]):
                if cart_item == item:
                    del self.carts[customer_id][i]
                    print(f"deleted {item} from the customer: {customer_id} cart.")
                    break
            else:
                print(f"{item} cannot be found in customer: {customer_id} cart.")
        else:
            print(f"there is no cart found for customer: {customer_id}.")

    def calculate_total(self, customer_id):
        if customer_id in self.carts:
            total = sum(price for item, price in self.carts[customer_id])
            print(f"current total amount for customer {customer_id}'s cart: {total:.2f} BGN")
        else:
            print(f"there is no card found for customer: {customer_id}.")

    def display_cart(self, customer_id):
        if customer_id in self.carts:
            print(f"Cart for customer {customer_id}:")
            for item, price in self.carts[customer_id]:
                print(f" - {item}: BGN{price}")
        else:
            print(f"No cart found for customer: {customer_id}.")

def main():
    cart = ShoppingCart()
    while True:
        action = input("Pick an option: (1) add item, (2) delete item, (3) show cumulative total, (4) display cart, (5) exit: ")
        if action == '1':
            customer_number = input("enter customer number: ")
            item = input("enter title of item: ")
            price = float(input("enter price of item: "))
            cart.add_item(customer_number, item, price)
        elif action == '2':
            customer_number = input("enter customer number: ")
            item = input("enter title of item: ")
            cart.remove_item(customer_number, item)
        elif action == '3':
            customer_number = input("enter customer number: ")
            cart.calculate_total(customer_number)
        elif action == '4':
            customer_number = input("enter customer number: ")
            cart.display_cart(customer_number)
        elif action == '5':
            print("exiting")
            break
        else:
            print("No valid option picked, try again.")

if __name__ == "__main__":
    main()
