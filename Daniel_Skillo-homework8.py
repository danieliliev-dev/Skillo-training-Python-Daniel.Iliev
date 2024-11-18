#Problem 0:
#Fix the mistakes in the following snippet:
#items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
#for item in items.keys()
#income = 0
#qty = input(f"How many {item}s have you sold? ")
#income = income + qty * items[item]
#print(f"\nThe income today was £{income:0.2f}")
items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
income = 0

for item in items.keys():  # Fixed: Added a colon at the end of this line
    qty = int(input(f"How many {item}s have you sold? "))  # Fixed: Convert input to an integer
    income += qty * items[item]  # This line is updated to use shorthand

print(f"\nThe income today was £{income:0.2f}")

#Problem 1:
#Rewrite the following function so it is exception safe
#def get_integer_input():
#num = int(input("Enter an integer: "))
#return num
#number = get_integer_input()
#print("You entered:", number)

def get_integer_input():
    while True:  # Loop until a valid integer is provided
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:  # Catch the exception if the input is not a valid integer
            print("Invalid input. Please enter a valid integer.")
number = get_integer_input()
print("You entered:", number)

#Problem 2:
#Research and understand how does selections sort work.
#Debug and fix the following code to make it correct
#def selection_sort(arr):
#for i in range(len(arr)):
#min_index = i
#for j in range(i + 1, len(arr)):
#if arr[i] < arr[min_index]:
#min_index = j
#arr[i], arr[min_index] = arr[min_index], arr[i]
#return arr
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:  # Compare current element with the min_index element
                min_index = j  # Update the index of the minimum element found
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


