#1. Create a Python script that reads a text file called "numbers.txt" containing integers and calculates their sum.


# script.py

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        # Read the contents and split by whitespace
        content = file.read()
        # Convert each number to an integer and return as a list
        numbers = list(map(int, content.split()))
    return numbers

def calculate_sum(numbers):
    return sum(numbers)

def main():
    filename = 'numbers.txt'
    numbers = read_numbers_from_file(filename)
    total_sum = calculate_sum(numbers)
    print(f'The sum of the numbers is: {total_sum}')

if __name__ == '__main__':
    main()

#2. Write a program that reads a text file, "words.txt," and counts the number of words in it.

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return 0

if __name__ == "__main__":
    filename = "words.txt"
    word_count = count_words_in_file(filename)
    print(f"The number of words in '{filename}' is: {word_count}")

#3. Create a Python script that prompts the user to enter student names and their corresponding scores, then stores this data in a CSV file called
#"student_scores.csv."

def main():

    with open('student_scores.csv', 'w') as file:

        file.write('Name,Score
                   ')

        while True:

            name = input("Enter the student's name (or type 'exit' to finish): ")
            if name.lower() == 'exit':
                break


            score = input(f"Enter the score for {name}: ")


            file.write(f'{name},{score}\n')

    print("Student scores have been saved to student_scores.csv.")


if __name__ == "__main__":
    main()

#4. Write a program that reads a CSV file called "employee_data.csv," and for each employee, calculates their total salary (considering base salary and
#bonuses) and saves it in a new CSV file called "total_salaries.csv."

def calculate_total_salaries(input_filename, output_filename):

    with open(input_filename, 'r') as infile:

        header = infile.readline().strip()

        result_lines = ["EmployeeID,TotalSalary"]


        for line in infile:

            data = line.strip().split(',')
            if len(data) < 3:
                continue


            employee_id = data[0]
            try:
                base_salary = float(data[1])  # Convert base salary to float
                bonus = float(data[2])  # Convert bonus to float
            except ValueError:
                continue  # If conversion fails, skip invalid line

            total_salary = base_salary + bonus

            result_lines.append(f"{employee_id},{total_salary:.2f}")
    with open(output_filename, 'w') as outfile:
        # Write each line from the result
        for line in result_lines:
            outfile.write(line + '\n')

calculate_total_salaries('employee_data.csv', 'total_salaries.csv')

#5. Design a program that reads a JSON file containing a list of products with names and prices. Calculate the total cost of all products and display it.
def read_and_calculate_total_cost(filename):

    with open(filename, 'r') as file:
        data = file.read()


    data = data.strip()


    if not (data.startswith("[") and data.endswith("]")):
        raise ValueError("Invalid JSON format: Should start with '[' and end with ']'")


    total_cost = 0.0


    products = data[1:-1].split("},")

    for product in products:

        product = product.strip().rstrip('}') + '}'


        if '"price":' in product:

            price_part = product.split('"price":')[1].strip()

            price = float(price_part.split(",")[0].strip())
            total_cost += price

    return total_cost


filename = 'products.json'
total = read_and_calculate_total_cost(filename)
print(f'Total cost of all products: ${total:.2f}')

#6. Write a Python script that reads a JSON file, "contacts.json," containing contact information (name, email, phone).
def read_contacts(filename):
    with open(filename, 'r') as file:
        data = file.read()


    data = data.strip()


    if data.startswith('[') and data.endswith(']'):
        data = data[1:-1]

        contacts = []
        for entry in data.split('},'):
            entry = entry.strip()
            if not entry.endswith('}'):
                entry += '}'

            entry = entry[1:-1]
            contact = {}
            for pair in entry.split(','):
                key_value = pair.split(':')
                if len(key_value) == 2:
                    key = key_value[0].strip().strip('\"')
                    value = key_value[1].strip().strip('\"')
                    contact[key] = value
            contacts.append(contact)
        return contacts
    else:
        return []


filename = 'contacts.json'
contacts = read_contacts(filename)
for contact in contacts:
    print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

#7. Create a CSV file, "student_data.csv," with student names and their corresponding JSON data containing exam scores. Write a program that reads the
#CSV file and calculates the average score for each student.


def average_scores_from_csv(file_name):

    with open(file_name, 'r') as file:

        lines = file.readlines()


        student_scores = {}

        for line in lines[1:]:  # Skip the header line

            data = line.strip().split(',', 1)
            name = data[0]
            scores_string = data[1].strip().strip('"')  # Remove quotes around the JSON-like string


            scores = {}
            scores_data = scores_string.lstrip('{').rstrip('}').split(', ')
            for item in scores_data:
                subject, score = item.split(': ')
                scores[subject.strip().strip('"')] = int(score.strip())


            student_scores[name] = scores


        averages = {}
        for name, scores in student_scores.items():
            average = sum(scores.values()) / len(scores)
            averages[name] = average

    return averages



file_name = "student_data.csv"

average_scores = average_scores_from_csv(file_name)


for student, avg_score in average_scores.items():
    print(f"{student}: {avg_score:.2f}")

#9. Provide an example XML file, "inventory.xml," that represents a list of products in a store. Write a Python program to read this XML file and print the
#names and prices of all products.

with open("inventory.xml", "r") as file:
    xml_content = file.read()

products = xml_content.split('</product>')

for product in products:
    if '<product>' in product:
        # Extract name and price
        name_start = product.find('<name>') + len('<name>')
        name_end = product.find('</name>')
        price_start = product.find('<price>') + len('<price>')
        price_end = product.find('</price>')

        name = product[name_start:name_end]
        price = product[price_start:price_end]

        # Print product name and price
        print(f'Product Name: {name}, Price: {price}')