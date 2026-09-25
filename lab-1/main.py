'''Python Final Assignment

Topics:
- Variables
- Basic Data Types
- Input and Output
- Type Conversion
- Arithmetic Operators
- Basic PEP 8
'''


# ==========================================
# Task 1 - Personal Information
# ==========================================

print("Task 1 - Personal Information")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years old.")


# ==========================================
# Task 2 - Basic Data Types
# ==========================================

print("\nTask 2 - Basic Data Types")

student_name = "Sheikh Muhammad Shameem"
student_age = 44
cgpa = 3.47
is_student = True

print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"CGPA: {cgpa}")
print(f"Student: {is_student}")


# ==========================================
# Task 3 - Input and Output
# ==========================================

print("\nTask 3 - Input and Output")

department = input("Enter your department: ")
university = input("Enter your university: ")

print("\nStudent Information")
print(f"Name: {student_name}")
print(f"Department: {department}")
print(f"University: {university}")


# ==========================================
# Task 4 - Type Conversion
# ==========================================

print("\nTask 4 - Type Conversion")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(f"First number: {number1}")
print(f"Second number: {number2}")
print(f"Sum: {number1 + number2}")


# ==========================================
# Task 5 - Arithmetic Operators
# ==========================================

print("\nTask 5 - Arithmetic Operators")

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")

if b != 0:
    print(f"Division: {a / b}")
    print(f"Floor Division: {a // b}")
    print(f"Modulus: {a % b}")
else:
    print("Division by zero is not allowed.")

print(f"Power: {a ** b}")


# ==========================================
# Task 6 - Electrical Power Calculation
# ==========================================

print("\nTask 6 - Electrical Power Calculation")

voltage = float(input("Enter voltage in volts: "))
current = float(input("Enter current in amperes: "))

power = voltage * current

print("\nElectrical Calculation")
print(f"Voltage: {voltage} V")
print(f"Current: {current} A")
print(f"Power: {power} W")


# ==========================================
# End of Assignment
# ==========================================

print("\nAssignment completed successfully.")