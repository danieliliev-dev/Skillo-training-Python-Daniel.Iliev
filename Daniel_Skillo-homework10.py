#0. Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backward).
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

input_text = input("Enter word or phrase")

if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome')
else:
    print(f'"{input_text}" is not a palindrome')

#1. Write a function that checks if a given number is prime or not.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


num = int(input("Enter a number"))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

#2. Write a program to reverse a given string without using string slicing.
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

input_text = input("Enter a string to reverse:")
print(f"The reversed string is {reverse_string(input_text)}")

#3. Create a program that checks if two given strings are anagrams of each other.
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams')
else:
    print(f'"{string1}" and "{string2}" are not anagrams')

#4. Write a program that counts the number of words in a given string.
def count_words(input_string):
    words = input_string.split()

    return len(words)

input_text = input("Enter a string")
word_count = count_words(input_text)
print(f"The number of words in the given string is:{word_count}")

#5. Create a program that reads a CSV file, "sales.csv," containing sales data,
# and a JSON file, "products.json," with product information.
# Calculate the total revenue for each product and save it in a new CSV file called "product_revenue.csv."

import csv
import json

def read_sales_data(csv_filename):
    sales_data = {}
    with open(csv_filename, mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            product_id = int(row['product_id'])
            quantity_sold = int(row['quantity_sold'])
            if product_id in sales_data:
                sales_data[product_id] += quantity_sold
            else:
                sales_data[product_id] = quantity_sold
    return sales_data


def read_product_data(json_filename):
    with open(json_filename, mode='r') as jsonfile:
        return json.load(jsonfile)


def calculate_revenue(sales_data, products):
    product_revenue = []
    product_dict = {product['product_id']: product for product in products}

    for product_id, quantity_sold in sales_data.items():
        if product_id in product_dict:
            product = product_dict[product_id]
            total_revenue = quantity_sold * product['price']
            product_revenue.append({
                'product_id': product_id,
                'name': product['name'],
                'total_revenue': total_revenue
            })
    return product_revenue


def write_product_revenue(csv_filename, revenue_data):
    with open(csv_filename, mode='w', newline='') as csvfile:
        fieldnames = ['product_id', 'name', 'total_revenue']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in revenue_data:
            writer.writerow(row)


def main():
    sales_data = read_sales_data('sales.csv')
    products = read_product_data('products.json')
    revenue_data = calculate_revenue(sales_data, products)
    write_product_revenue('product_revenue.csv', revenue_data)
    print("Revenue data has been written to 'product_revenue.csv'.")


if __name__ == "__main__":
    main()

#6. Develop a Python script that reads a JSON file called "inventory.json"
# with information about products and their quantities. Create a new CSV file, "low_stock.csv,"
# containing the names of products with a quantity less than 10.

import json
import csv

def read_inventory_data(json_filename):
    with open(json_filename, mode='r') as jsonfile:
        return json.load(jsonfile)

def filter_low_stock(inventory_data):
    low_stock_items = []
    for product in inventory_data:
        if product['quantity'] < 10:
            low_stock_items.append(product['name'])
    return low_stock_items

def write_low_stock_to_csv(csv_filename, low_stock_items):
    with open(csv_filename, mode='w', newline='') as csvfile:
        fieldnames = ['product_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in low_stock_items:
            writer.writerow({'product_name': item})

def main():
    inventory_data = read_inventory_data('inventory.json')

    low_stock_items = filter_low_stock(inventory_data)

    write_low_stock_to_csv('low_stock.csv', low_stock_items)

    print("Low stock products have been written to 'low_stock.csv'.")

if __name__ == "__main__":
    main()

#7. Write a program that is given a number and an array
#and checks if there is a pair of numbers in the array that has a sum equal to the given number. ( two-sum problem )
def has_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

target = int(input("Enter the target number"))
arr = list(map(int, input("Enter the array elements separated by spaces:").split()))

if has_pair_with_sum(arr, target):
    print("There is a pair with the given sum")
else:
    print("There is no pair with the given sum")

