# 1. Create a list with the numbers from 1 to 10 and print it.
numbers = list(range(1, 11))
print(numbers)

# 1.1. Create a list with the numbers from 1 to 1000 and print it.
numbers = list(range(1, 1001))
print(numbers)

# 2. Reverse the order of the elements in the list from problem 1 and print the result.
numbers = list(range(1, 11))
numbers.reverse()
print(numbers)

# 3. Given a list of words, create a new list containing the lengths of each word.
words = ["nescafe", "kitkat", "maggi", "purina", "lion"]
lengths = [len(word) for word in words]
print(lengths)

# 3.1. Given a list of words, create a new dictionary mapping every word to it's length.
words = ["nescafe", "kitkat", "maggi", "purina", "lion"]
word_length_dict = {word: len(word) for word in words}
print(word_length_dict)

# 4. Write a function that takes a list and returns the sum of all even numbers in the list.
def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)
list = [1, 2, 3, 4, 5]
result = sum_even_numbers(list)
print(result)

# 5. Given a tuple of integers, find the maximum and minimum values without using built-in functions.
def find_max_min(numbers):
    max_value = numbers[0]
    min_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value

tuple = (22, 36, 92, 131, 428)
max_value, min_value = find_max_min(tuple)
print("Max:", max_value)
print("Min:", min_value)

# 6. Implement a basic queue structure ( as a global var ) by defining two functions `enqueue` and `dequeue.
queue = []
def enqueue(product):
    "insert product at the end of the queue"
    queue.append(product)

def dequeue():
    "remove product from end of the queue"
    if not is_empty():
        return queue.pop(0)
    else:
        raise IndexError("dequeue product from an empty queue")

def is_empty():
    "Check queue if empty."
    return len(queue) == 0

enqueue(893)
enqueue(42)
enqueue(1001)

print("dequeued:", dequeue())
print("dequeued:", dequeue())
print("queue empty?", is_empty())
print("dequeued:", dequeue())
print("queue empty?", is_empty())


# 7. Create a dictionary that maps students to their bank account number. Some students may have multiple bank accounts.
student_accounts = {
    "Tosho": ["5500"],
    "Penka": ["200", "150", "1001"],
    "Ginka": ["750"]
}

for student, accounts in student_accounts.items():
    print(f"{student}: {', '.join(accounts)}")

# 8. Think of a function that can hash lists. Implement it and test it.
def hash_list(enter_list):
    list_pair = tuple(enter_list) # not working
    return hash(list_pair)

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list3 = [4, 3, 2, 1]

hash1 = hash_list(list1)
hash2 = hash_list(list2)
hash3 = hash_list(list3)

print(f"Hash list 1: {hash1}")
print(f"Hash list 2: {hash2}")
print(f"Hash list 3: {hash3}")
print(f"Hash 1 == Hash 2: {hash1 == hash2}")
print(f"Hash 1 == Hash 3: {hash1 == hash3}")

# 9. Write a function that counts the frequency of each word in a given string
# (copy the first paragraph of an online article, for example) and returns a dict with the result.
def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency
text = """Nestlé is a global food and beverage leader, known for its commitment to quality and innovation. Founded in 1866, the company offers a wide range of products, including dairy, coffee, and nutrition items. Nestlé emphasizes sustainability and health, aiming to enhance lives through its diverse offerings and responsible practices."""
result = word_frequency(text)
print(result)

# 10. Create two sets with some common elements and find their intersection.
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {4, 4, 2}
intersection = set1.intersection(set2)
print("Intersection:", intersection)

# 11. Given two sets, write a function that determines if one set is a subset of the other. Do not use `<` or `>`
def is_subset(set_a, set_b):
    for element in set_a:
        if element not in set_b:
            return False
    return True
set1 = {1, 2, 3, 4, 6, 7, 8, 9, 10}
set2 = {1, 2, 3}
result = is_subset(set1, set2)
print(f"Is set1 a subset of set2? {result}")
set3 = {1, 9}
result = is_subset(set3, set2)
print(f"Is set3 a subset of set2? {result}")

# 12. Write a function to remove duplicates from a list using a set.
def remove_duplicates(enter_list):
    unique_list = list(set(enter_list))
    return unique_list

setlist = [1, 2, 3, 3, 3, 4, 4, 5, 1, 1]
result = remove_duplicates(setlist)
print("removed duplicates", result)

# 13. Use list comprehension to create a list of the squares of even numbers from 1 to 30.
squares_of_even_num = [num ** 2 for num in range(1, 31) if num % 2 == 0]
print(squares_of_even_num)

# 14. Given a list of words, create a dictionary where the keys are the words and the values are their lengths, using dictionary comprehension.
words = ["Chocolate", "Cookies", "Vanilla", "Mint"]
word_length_dict = {word: len(word) for word in words}
print(word_length_dict)

# 15. Write a program that generates a set of prime numbers less than 100 using list comprehensions and sets.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = {num for num in range(2, 100) if is_prime(num)}
print(prime_numbers)
