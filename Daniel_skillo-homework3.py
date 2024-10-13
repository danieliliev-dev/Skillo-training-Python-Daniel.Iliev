# Problem 0:Write a program that takes an integer input from the user
# and checks if it's odd or even. Use an if-else statement to print the result.
number = int(input("please enter integer: "))
# Check if the number is odd or even
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Problem 1:Write a Python program to find the sum of all even numbers from 1 to 100 using a loop.
# Make use of control flow constructs like the for loop and conditional statements.
total_sum = 0
# Looping through inbetween 1 through 100
for number in range(1, 101):
    # Check if number is even
    if number % 2 == 0:
        total_sum += number
# get result
print(f"total sum from all even numbers 1 through 100 is {total_sum}.")

# Problem 2:Write a Python script that prompts the user in the console a simple problem
# ( how much does 5 + 17 equal to ) until the user provides a correct answer.
answer = 5 + 17
while True:
    user_answer = int(input("How much is 5 + 17? "))
    if user_answer == answer:
        print("that's right!")
        break
    else:
        print("WRONG!")

# Problem 3: Write a Python script that iterates over the first 1000 numbers
# and prints "Fizz" if the number is divisible by 3, "Buzz" if it's divisible by 5,
# and "FizzBuzz" if it's divisible by both 3 and 5.
for number in range(1, 1001):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Problem 4: Design a Python program that simulates a simple guessing game.
# The program should generate a random number between 1 and 100 and ask the user to guess it.
# Provide hints like "Too high" or "Too low" until the user
# guesses the correct number. Use a while loop for this game.
import random

random_number = random.randint(1, 100)
while True:
    guess = int(input("Try to guess a number between 1 and 100: "))
    if guess < random_number:
        print("aim higher")
    elif guess > random_number:
        print("aim lower")
    else:
        print("Well done, you guessed correctly!")
        break

# Problem 5: Modify problem 2 so that every time the user is prompted the problem is different.
# Think of a way to design that and come up with a proper solution for that.
# Define the correct answer
answer = 5 + 17
while True:
    user_answer = int(input("How much is 5 + 17? "))
    if user_answer == answer:
        print("that's right!")
        break
    else:
        print("WRONG!")
import random

while True:
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    answer = number1 + number2
    user_answer = int(input(f"How much is {number1} + {number2} ? "))
    if user_answer == answer:
        print("that's right!")
        break
    else:
        print("WRONG!")

# Problem 6: Write a Python program that takes an integer input
# from the user and prints the multiplication table for that number from 1 to 10 using a for loop.
# Get an integer input from the user
number = int(input("please enter integer: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Problem 7: Create a Python program that checks if a given integer is a prime number.
# Use a for loop to iterate through possible divisors and use an if-else statement to determine if it's prime.
# Get an integer input from the user
number = int(input("please integer: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(f"{number} is not prime number")
            break
    else:
        print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")

# Problem 8: Pattern Printing
# Write a program that takes an integer 'n' as input and prints the following pattern using nested for loops:
# Expected output for input “5”:
# 1
# 12
# 123
# 1234
# 12345
n = int(input("please enter integer: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
