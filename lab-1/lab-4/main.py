"""
NSU Python - Lab Assignment 04
Topics: while Loops, Typing (Type Hinting), Identity, and Functions
Student Name: Sheikh Muhammad Shameem.
Student ID:
Course: Programming in Python
"""""""""

# ==============================================================================
# Task 1 - Electrical Capacitor Voltage Decay (while Loop)
# ==============================================================================
# Description: Calculate the discharging voltage of a capacitor until it drops below 1V.
# Standard formula simulation using a while loop.

def monitor_voltage(initial_voltage: float) -> None:
    voltage = initial_voltage
    time_sec = 0
    print(f"Starting discharge from {voltage}V...")
    
    while voltage >= 1.0:
        print(f"Time: {time_sec}s | Voltage: {voltage:.2f}V")
        voltage = voltage * 0.8  # Decreasing voltage by 20% each second
        time_sec += 1
        
    print("Capacitor Discharged (Voltage < 1V)!")

# Test Task 1
# monitor_voltage(10.0)


# ==============================================================================
# Task 2 - Resistance Series Sum Calculator (Functions & Type Hinting)
# ==============================================================================
# Description: Function that takes two resistor values and returns equivalent series resistance.

def calculate_series_resistance(r1: float, r2: float) -> float:
    total_resistance = r1 + r2
    return total_resistance

# Test Task 2
# res = calculate_series_resistance(150.5, 220.0)
# print("Total Resistance in Series:", res, "Ohms")


# ==============================================================================
# Task 3 - Checking Object Identity (Identity Operators)
# ==============================================================================
# Description: Demonstrates 'is' and 'is not' operators to check if two variables point 
# to the same memory location or object.

def check_signal_identity():
    signal_a = [5, 10, 15]
    signal_b = [5, 10, 15]
    signal_c = signal_a

    print("signal_a is signal_b:", signal_a is signal_b)  # False, different memory
    print("signal_a is signal_c:", signal_a is signal_c)  # True, same reference
    print("signal_a == signal_b:", signal_a == signal_b)  # True, same values

# Test Task 3
# check_signal_identity()


# ==============================================================================
# Task 4 - Sum of Odd Numbers (while Loop)
# ==============================================================================
# Description: Ask the user for a limit and sum up all odd numbers from 1 to that limit.

def sum_odd_numbers():
    limit = int(input("Enter a positive integer limit: "))
    count = 1
    total_sum = 0
    
    while count <= limit:
        if count % 2 != 0:
            total_sum += count
        count += 1
        
    print(f"The sum of all odd numbers up to {limit} is: {total_sum}")

# Test Task 4
# sum_odd_numbers()


# ==============================================================================
# Task 5 - LED Flashing Counter (while Loop & Functions)
# ==============================================================================
# Description: Simulate an LED blinking a specified number of times.

def blink_led(times: int) -> None:
    current_count = 1
    while current_count <= times:
        print(f"Blink {current_count}: LED ON -> LED OFF")
        current_count += 1
    print("Blinking sequence completed.")

# Test Task 5
# blink_led(5)


# ==============================================================================
# Task 6 - Ohm's Law Power Calculation (Type Hints & Functions)
# ==============================================================================
# Description: Function to calculate Power (P = V * I) given Voltage and Current.

def calculate_power(voltage: float, current: float) -> float:
    power = voltage * current
    return power

# Test Task 6
# p = calculate_power(220.0, 2.5)
# print(f"Calculated Power: {p} Watts")


# ==============================================================================
# Task 7 - Reverse Number Printer (while Loop)
# ==============================================================================
# Description: Takes a positive integer from user and prints its digits in reverse.

def reverse_digits():
    num = int(input("Enter a number to reverse: "))
    reversed_num = 0
    
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10
        
    print("Reversed Number:", reversed_num)

# Test Task 7
# reverse_digits()


# ==============================================================================
# Task 8 - Type Checking and Validation (Typing)
# ==============================================================================
# Description: Function that validates if the input is integer or float, then converts to string.

def format_sensor_reading(value: float) -> str:
    if type(value) is int or type(value) is float:
        return f"Sensor Data: {float(value):.2f} Units"
    else:
        return "Invalid Input Type!"

# Test Task 8
# print(format_sensor_reading(23.456))
# print(format_sensor_reading("23.45"))


# ==============================================================================
# Task 9 - Battery Overheat Safety Warning (while Loop)
# ==============================================================================
# Description: Monitor temperature rise until it exceeds safe limit.

def monitor_battery_temp(start_temp: float, max_safe_temp: float) -> None:
    current_temp = start_temp
    print("Monitoring battery temperature...")
    
    while current_temp <= max_safe_temp:
        print(f"Status Normal: Current Temperature = {current_temp}°C")
        current_temp += 3.5  # Temperature increasing
        
    print(f"WARNING! Critical Temperature Reached: {current_temp}°C! System Shutdown!")

# Test Task 9
# monitor_battery_temp(30.0, 45.0)


# ==============================================================================
# Task 10 - Factorial Calculator using while Loop
# ==============================================================================
# Description: Calculates the factorial of a given positive integer.

def calculate_factorial(n: int) -> int:
    result = 1
    counter = n
    
    while counter > 1:
        result *= counter
        counter -= 1
        
    return result

# Test Task 10
# number = 5
# print(f"Factorial of {number} is: {calculate_factorial(number)}")