'''
NSU Python Program - Lab 08

Function in Practice: To understand Python file handling operations including opening, 
reading, writing, appending, processing data from files, handling relative paths,
text encoding, missing files, and calculating the average of numerical data.


Complite Task: 1-16
Use only concepts covered in Lecture 08 earlier lectures.


Task 1: Variables and Files
'''
print("Task-1")

student_name = "Shameem"
student_id = 103
department = "Electrical Engineering"

with open("student.txt", "w", encoding="utf-8") as filewrite:
    filewrite.write("Student Name: " + student_name + "\n")
    filewrite.write("Student ID: " + str(student_id) + "\n")
    filewrite.write("Department: " + department + "\n")

print("Student information saved successfully.")

#Task 2: First Read — Reading the Whole File

print("Task-2")


file = open("marks.txt", "r")

data = file.read()

print(data)

file.close()

#Task 3: open() Arguments

print("Task-3")


file = open("data.txt", "r", encoding="utf-8")

content = file.read()

print(content)

file.close()

#Task 4: Different File Modes

print("Task-4")


file = open("example.txt", "w")
file.write("Python File Handling")
file.close()

print("File created successfully.")

# Task 5: read() — Read the Whole File

print("Task-5")

with open("numbers.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)

# Task 6: Reading One Time

print("Task-6")


with open("data.txt", "r") as file:

    first_read = file.read()
    second_read = file.read()

print("First Read:")
print(first_read)

print("Second Read:")
print(second_read)

# Task 7: Reading as a List

print("Task-7")


with open("marks.txt", "r") as file:
    lines = file.readlines()

print(lines)

# Task 8: Iterating Over a File

print("Task-8")


with open("subjects.txt", "r") as file:

    for line in file:
        print(line.strip())

# Task 9: Appending with a

print("Task-9")


with open("students.txt", "a") as file:
    file.write("Rahim\n")

print("New student added.")

# Task 10: Writing Text with w

print("Task-10")


with open("message.txt", "w") as file:
    file.write("Welcome to Python.\n")
    file.write("This is file handling.")

print("Data written successfully.")

# Task 11: New Lines and Output

print("Task-11")


with open("report.txt", "w") as file:
    file.write("Student Report\n")
    file.write("----------------\n")
    file.write("Name: Shameem\n")
    file.write("Department: EEE\n")
    file.write("Result: Passed\n")

print("Report generated.")

# Task 12: Text Encoding

print("Task-12")


text = "Bangladesh Python Programming Learn"

with open("bangla.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Bangla text saved successfully.")

# Task 14: Missing Files

print("Task-14")


try:
    with open("result.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("The file was not found.")

# Task 15: Read, Process and Average from a File

print("Task-15")


with open("marks.txt", "r") as file:
    lines = file.readlines()

marks = []

for line in lines:
    mark = float(line.strip())
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)

# Task-16: Student Marks File Processing System

print("Task-16")

# Student Marks File Processing System

file_path = "data/marks.txt"

try:
    # Write marks into the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("75\n")
        file.write("82\n")
        file.write("90\n")
        file.write("68\n")
        file.write("85\n")

    # Append another mark
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("95\n")

    # Read the whole file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print("Complete File Content:")
    print(content)

    # Read file as a list
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    marks = []

    # Process each line
    for line in lines:
        mark = float(line.strip())
        marks.append(mark)

    # Calculate total and average
    total = sum(marks)
    average = total / len(marks)

    print("Marks:", marks)
    print("Total Marks:", total)
    print("Number of Students:", len(marks))
    print("Average Marks:", average)

except FileNotFoundError:
    print("Error: The file was not found.")

except ValueError:
    print("Error: Invalid data found in the file.")







