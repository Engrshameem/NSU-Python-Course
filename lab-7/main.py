# NSU Python program - Lab 07

# Function in Practice: The objective of this program is to demonstrate  string sequences, indexing,
# slicing, length, iteration, case conversion, text replacement, prefix and suffix checking,
# counting, substring searching, string cleaning, character classes, regular expressions, 
# search(), match(), fullmatch(), and the regex quantifiers ?, +, and *.5,

# Complete Task 1-15
# Use only concepts covered in Lecture o7 and earlier lectures.


# Task - 01 String is a Sequence

print("Task-1")

text = "Python"

print(text[0])
print(text[1])
print(text[5])

# Task - 02 Indexing and Slicing

print("Task-2")

word = "Electrical"

print(word[0])
print(word[-1])
print(word[0:5])
print(word[2:7])
print(word[::-1])

# Task 03  Length and Iteration

print("Task-3")


name = "Shameem"

print("Length:", len(name))

for letter in name:
    print(letter)

# Task 04  Changing Letter Case

print("Task-4")


text = "Python Programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

# Task 05  Replacing Text

print("Task-5")


sentence = "I study Python"

new_sentence = sentence.replace("Python", "Artificial Intelligence")

print(new_sentence)

# Task 06  Prefix, Suffix and Count

print("Task-6")


filename = "assignment_python.py"

print(filename.startswith("assignment"))
print(filename.endswith(".py"))
print(filename.count("p"))

# Task 07  Searching for a Substring

print("Task-7")


sentence = "Python is useful for data analysis"

print("data" in sentence)
print(sentence.find("useful"))
print(sentence.find("Java"))

# Task 08  Quick Check: Clean a Name

print("Task-8")


name = "   Sheikh Muhammad Shameem   "

clean_name = name.strip().title()

print(clean_name)

# Task 09  Characters and the Dot

print("Task-9")


import re

text = "Cat Cot Cut"

result = re.findall(r"C.t", text)

print(result)

# Task 10  Character Classes

print("Task-10")


import re

text = "Python 123 ABC"

print(re.findall(r"[A-Z]", text))
print(re.findall(r"[a-z]", text))
print(re.findall(r"[0-9]", text))

# Task 11  search()

print("Task-11")


import re

text = "My student ID is CSE12345"

result = re.search(r"\d+", text)

if result:
    print("Number found:", result.group())
else:
    print("Number not found")

# Task 12  match()

print("Task-12")


import re

text = "Python Programming"

result = re.match(r"Python", text)

if result:
    print("Match found")
else:
    print("No match")

# Task 13  fullmatch()

print("Task-13")


import re

student_id = "EEE2026123"

result = re.fullmatch(r"EEE\d{7}", student_id)

if result:
    print("Valid Student ID")
else:
    print("Invalid Student ID")

# Task 14  Checking a Student ID

print("Task-14")


import re

student_id = input("Enter Student ID: ")

pattern = r"EEE\d{7}"

if re.fullmatch(pattern, student_id):
    print("Valid Student ID")
else:
    print("Invalid Student ID")

# Task 15  Important String Methods

print("Task-15")


text = "  Python Programming  "

print(text.strip())
print(text.replace("Python", "Java"))
print(text.split())
print("-".join(["Python", "Programming"]))

# Task 16  Regex ?, + , and*

print("Task-16")


import re

text = "color colour colouur"

print(re.findall(r"colou?r", text))
print(re.findall(r"colou+r", text))
print(re.findall(r"colou*r", text))

