""
NSU Python - Lab 03
Conditions and for Loops

Complete Tasks 1-10.
Use only concepts covered in Lecture 03.
""

# ==============================================================================
# Task 1 - Resistor Tolerable Voltage Checker (EEE)
# ==============================================================================
# Ask the user to enter the operating voltage (V).
# Print "Normal" if voltage is <= 5V, "Warning: High Voltage" if between 6V and 12V,
# and "Danger: Overvoltage" if > 12V.
#
# Example:
# Input: 15
# Output: Danger: Overvoltage

# code below:

voltage = float(input("Enter voltage (V): "))

if voltage <= 5:
    print("Normal")
elif voltage <= 12:
    print("Warning: High Voltage")
else:
    print("Danger: Overvoltage")


# ==============================================================================
# Task 2 - AC Signal Peak Voltage Classification (EEE)
# ==============================================================================
# Ask the user for maximum peak voltage (Vp).
# Print "Low Voltage Circuit" if Vp < 50, "Medium Voltage Circuit" if 50 <= Vp <= 250,
# and "High Voltage Circuit" if Vp > 250.
#
# Example:
# Input: 220
# Output: Medium Voltage Circuit

# code below:

vp = float(input("Enter peak voltage (Vp): "))

if vp < 50:
    print("Low Voltage Circuit")
elif vp <= 250:
    print("Medium Voltage Circuit")
else:
    print("High Voltage Circuit")


# ==============================================================================
# Task 3 - LED Diode State Determination (EEE)
# ==============================================================================
# Ask the user for the forward bias voltage (Vf) across an LED.
# Print "OFF" if Vf < 0.7V, "ON (Normal Brightness)" if 0.7V <= Vf <= 2.2V,
# and "BURNT (Overcurrent)" if Vf > 2.2V.
#
# Example:
# Input: 1.8
# Output: ON (Normal Brightness)

# code below:

vf = float(input("Enter forward voltage (Vf): "))

if vf < 0.7:
    print("OFF")
elif vf <= 2.2:
    print("ON (Normal Brightness)")
else:
    print("BURNT (Overcurrent)")


# ==============================================================================
# Task 4 - Total Power Consumption of N Electrical Appliances (EEE)
# ==============================================================================
# Ask the user for the number of appliances (N).
# Use a for loop to read the power rating (Watts) of each appliance and print the total power.
#
# Example:
# Input: N = 3, Power = 100, 50, 150
# Output: Total Power: 300.0 W

# code below:

n = int(input("Enter total number of appliances: "))
total_power = 0.0

for i in range(1, n + 1):
    power = float(input(f"Enter power for appliance {i} (W): "))
    total_power += power

print(f"Total Power: {total_power} W")


# ==============================================================================
# Task 5 - Equivalent Resistance Calculation for N Series Resistors (EEE)
# ==============================================================================
# Ask the user for the number of resistors connected in series (N).
# Use a for loop to take the resistance value (Ohms) for each resistor and calculate Req.
#
# Example:
# Input: N = 3, R = 10, 20, 30
# Output: Equivalent Series Resistance: 60.0 Ohms

# code below:

n = int(input("Enter number of resistors in series: "))
req = 0.0

for i in range(1, n + 1):
    r = float(input(f"Enter resistance R{i} (Ohms): "))
    req += r

print(f"Equivalent Series Resistance: {req} Ohms")


# ==============================================================================
# Task 6 - Grade Calculator Based on Score
# ==============================================================================
# Ask the user to enter numerical marks (0-100).
# Print "Passed with Distinction" if marks >= 80, "Passed" if 50 <= marks < 80,
# and "Failed" if marks < 50.
#
# Example:
# Input: 85
# Output: Passed with Distinction

# code below:

marks = float(input("Enter student marks: "))

if marks >= 80:
    print("Passed with Distinction")
elif marks >= 50:
    print("Passed")
else:
    print("Failed")


# ==============================================================================
# Task 7 - Temperature State Classifier
# ==============================================================================
# Ask the user to enter temperature in Celsius.
# Print "Freezing" if temp < 0, "Moderate" if 0 <= temp <= 30, and "Hot" if temp > 30.
#
# Example:
# Input: -3
# Output: Freezing

# code below:

temp = float(input("Enter temperature (°C): "))

if temp < 0:
    print("Freezing")
elif temp <= 30:
    print("Moderate")
else:
    print("Hot")


# ==============================================================================
# Task 8 - Sum of First N Positive Even Numbers
# ==============================================================================
# Ask the user for a positive integer N.
# Use a for loop to calculate and print the sum of the first N even numbers.
#
# Example:
# Input: 4 (Evens: 2, 4, 6, 8)
# Output: Sum of first 4 even numbers: 20

# code below:

n = int(input("Enter N: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += (2 * i)

print(f"Sum of first {n} even numbers: {total_sum}")


# ==============================================================================
# Task 9 - Multiplication Table Generator
# ==============================================================================
# Ask the user to enter an integer.
# Use a for loop to print its multiplication table from 1 to 10.
#
# Example:
# Input: 5
# Output: 5 x 1 = 5 ... 5 x 10 = 50

# code below:

num = int(input("Enter an integer for multiplication table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# ==============================================================================
# Task 10 - Factorial Calculation of a Number
# ==============================================================================
# Ask the user to enter a non-negative integer.
# Use a for loop to calculate its factorial.
#
# Example:
# Input: 5
# Output: Factorial: 120

#  code below:

num = int(input("Enter a non-negative integer: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("Factorial: 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial: {factorial}")