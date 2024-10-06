#1.Write a Python script that prints "Hello, World!" to the console.
print("Hello, World!")
#2.Create variables to store your name, age, and favorite color.
#Then, print out a message using these variables (e.g., "My name is [name], I am [age] years old, and my favorite color is [color].").
name = "Daniel"
age = 32
favorite_color = "orange"
print(f"My name is {name}, I am {age} years old, and my favorite color is {favorite_color}.")
#3.Write a program that calculates the area of a rectangle. Prompt the user to enter the length and width, calculate the area, and then print it.
print ("enter length and width of triangle and calculate their area")
width = float(input("Enter length in of the rectangle"))
length = float(input("Enter the width of the rectangle"))
area = width*length
print(f"Area of the rectangle is {area} square unit(s)")
#4.Write a program that converts temperatures from Fahrenheit to Celsius.
# Prompt the user to enter a temperature in Fahrenheit and then print out the equivalent temperature in Celsius.
fahrenheit = float(input("enter temperature in fahrenheit degrees and get equivalent in celsius"))
celsius = (fahrenheit - 32) * 5 / 9
print(f"temperature in Celsius is {celsius:.2f}°C.")
#5.Create a program that asks the user to enter two numbers and then prints out the sum, difference, product, and quotient of those numbers.
print("enter two numbers and display their sum,difference,product and quotient")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
sum_result = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2 if number2 != 0 else "undefined (Divide by zero)"
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
#6.Write a program that prompts the user to enter a radius and then calculates and prints the area and circumference of a circle with that radius.
radius = float(input("Enter circle radius and receive its area and circumference"))
area = (22/7) * radius ** 2
circumference = 2 * (22/7) * radius
print(f"The area of the circle is {area:.2f} square unit(s).")
print(f"The circumference of the circle is {circumference:.2f} unit(s).")
#7.Create a program that checks whether a given number is even or odd. Prompt the user to enter a number and then print out whether it's even or odd.
print("Enter a number and see if it is odd or even")
number = int(input("enter number"))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
#8.Write a program that prompts the user to enter their age and then determines and prints out whether they are eligible to vote (i.e., if they are 18 or older).
print("Enter age and check if eligible to vote or not.")
age = int(input("Age:"))
if age <= 18 <= 130:
    print("Eligible")
elif age > 130:
    print("Age is above 130, possibly not alive, but able to vote")
else:
    print("age is below 18 - cannot vote yet")
#9.Create a program that prompts the user to enter a string and then prints out the length of the string.
user_string = input("enter string to show length in symbol amount")
string_length = len(user_string)
print("string length is:", string_length)
#10.Write a program that prompts the user to enter two strings and then concatenates them together (i.e., joins them into one string) and prints out the result.
print("Enter two strings and get their concatenated value")
string1 = input("first string: ")
string2 = input("second string: ")
concatenate = string1 + string2
print("concatenated/joined string:", concatenate)