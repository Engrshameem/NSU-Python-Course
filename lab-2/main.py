"""
Lab 02 – Python Basics II

Assignment:
Student Academic Performance and Personal Information Analyzer

Topics:
- Built-in functions
- Assignment and augmented assignment
- Operator precedence
- Type conversion
- Strings
- print() options
- Collections
- Mutable and immutable objects
- Formatted output
- Basic PEP 8
- Reading common errors

Restrictions:
- No if
- No for
- No while
- No user-defined functions
"""

print("==================================================")
print("   STUDENT ACADEMIC PERFORMANCE ANALYZER")
print("==================================================")

# --------------------------------------------------
# Task 1 – Student Information and Strings
# --------------------------------------------------

student_name = "Sheikh Muhammad Shameem"
student_id = "PY2026-001"
department = "Electrical and Electronic Engineering"

print("\nTask 1 – Student Information")
print("Name:", student_name)
print("Student ID:", student_id)
print("Department:", department)

# String operations
full_name = student_name
name_length = len(full_name)
name_upper = full_name.upper()
name_lower = full_name.lower()

print("Name length:", name_length)
print("Uppercase:", name_upper)
print("Lowercase:", name_lower)


# --------------------------------------------------
# Task 2 – Collections
# --------------------------------------------------

print("\nTask 2 – Collections")

marks = [78, 85, 69, 92, 88]
subjects = ("Python", "Mathematics", "Programming",
            "Database", "English")

skills = {"Python", "Programming", "Problem Solving"}

student = {
    "name": student_name,
    "id": student_id,
    "department": department
}

print("Marks:", marks)
print("Subjects:", subjects)
print("Skills:", skills)
print("Student information:", student)


# --------------------------------------------------
# Task 3 – Built-in Functions
# --------------------------------------------------

print("\nTask 3 – Built-in Functions")

total_marks = sum(marks)
highest_mark = max(marks)
lowest_mark = min(marks)
number_of_subjects = len(marks)
sorted_marks = sorted(marks)

average_mark = total_marks / number_of_subjects

print("Total marks:", total_marks)
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)
print("Number of subjects:", number_of_subjects)
print("Sorted marks:", sorted_marks)
print("Average mark:", round(average_mark, 2))


# --------------------------------------------------
# Task 4 – Assignment and Augmented Assignment
# --------------------------------------------------

print("\nTask 4 – Assignment and Augmented Assignment")

study_hours = 4

print("Initial study hours:", study_hours)

study_hours += 2
print("After += 2:", study_hours)

study_hours -= 1
print("After -= 1:", study_hours)

study_hours *= 2
print("After *= 2:", study_hours)

study_hours /= 2
print("After /= 2:", study_hours)


# --------------------------------------------------
# Task 5 – Operator Precedence
# --------------------------------------------------

print("\nTask 5 – Operator Precedence")

a = 10
b = 5
c = 2

result_1 = a + b * c
result_2 = (a + b) * c
result_3 = a ** c + b
result_4 = a + b - c * 2

print("a + b * c =", result_1)
print("(a + b) * c =", result_2)
print("a ** c + b =", result_3)
print("a + b - c * 2 =", result_4)


# --------------------------------------------------
# Task 6 – Type Conversion
# --------------------------------------------------

print("\nTask 6 – Type Conversion")

age_text = "44"
score_text = "87.5"

age = int(age_text)
score = float(score_text)

age_as_float = float(age)
score_as_integer = int(score)

print("Original age:", age_text)
print("Converted age:", age)
print("Age as float:", age_as_float)

print("Original score:", score_text)
print("Converted score:", score)
print("Score as integer:", score_as_integer)


# --------------------------------------------------
# Task 7 – print() Options
# --------------------------------------------------

print("\nTask 7 – print() Options")

print("Python", "Basics", "II", sep=" | ")

print("Student information:", end=" ")
print(student_name)

print("Marks:", end=" ")
print(marks)


# --------------------------------------------------
# Task 8 – Mutable and Immutable Objects
# --------------------------------------------------

print("\nTask 8 – Mutable and Immutable Objects")

# List is mutable
mutable_marks = [70, 80, 90]

print("Original list:", mutable_marks)

mutable_marks[0] = 75

print("Modified list:", mutable_marks)

# Tuple is immutable
immutable_subjects = ("Python", "Math", "English")

print("Original tuple:", immutable_subjects)

# A new tuple is created instead of modifying the old tuple
new_subjects = immutable_subjects + ("Database",)

print("New tuple:", new_subjects)


# --------------------------------------------------
# Task 9 – Formatted Output
# --------------------------------------------------

print("\nTask 9 – Formatted Output")

percentage = (total_marks / 500) * 100

print(f"Student Name : {student_name}")
print(f"Student ID   : {student_id}")
print(f"Total Marks  : {total_marks}")
print(f"Average Mark : {average_mark:.2f}")
print(f"Percentage   : {percentage:.2f}%")


# --------------------------------------------------
# Task 10 – Additional Built-in Functions
# --------------------------------------------------

print("\nTask 10 – Additional Built-in Functions")

numbers = [12, 7, 19, 5, 14]

print("Numbers:", numbers)
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Absolute value:", abs(-25))
print("Rounded value:", round(15.6789, 2))


# --------------------------------------------------
# Task 11 – Collection Operations
# --------------------------------------------------

print("\nTask 11 – Collection Operations")

marks_copy = marks.copy()

print("Original marks:", marks)
print("Copied marks:", marks_copy)

marks_copy.append(95)

print("After append:", marks_copy)

unique_marks = set(marks_copy)

print("Unique marks:", unique_marks)


# --------------------------------------------------
# Task 12 – Final Summary
# --------------------------------------------------

print("\n==================================================")
print("              FINAL SUMMARY")
print("==================================================")

print(f"Student       : {student_name}")
print(f"Department    : {department}")
print(f"Subjects      : {number_of_subjects}")
print(f"Total Marks   : {total_marks}")
print(f"Highest Mark  : {highest_mark}")
print(f"Lowest Mark   : {lowest_mark}")
print(f"Average Mark  : {average_mark:.2f}")
print(f"Percentage    : {percentage:.2f}%")
