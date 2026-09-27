"""
NSU Python - Lab 05
Functions in Practice: Arguments, Recursion, math, and List Methods

Complete Tasks 1-10.
Use only concepts covered in Lecture 05 and earlier lectures.
Do not use lambda, sorted(), filter(), or map() in this lab.
"""

# ==============================================================================
# Task 1 - Positional and Keyword Arguments (Ohm's Law Calculation)
# ==============================================================================
# Create a function calculate_voltage(current, resistance) that calculates voltage.

def calculate_voltage(current, resistance):
    # Formula: V = I * R
    v = current * resistance
    return v

# Calling using positional arguments
v1 = calculate_voltage(2.5, 10)
print("Voltage (Positional):", v1, "V")

# Calling using keyword arguments
v2 = calculate_voltage(resistance=15, current=1.2)
print("Voltage (Keyword):", v2, "V")


# ==============================================================================
# Task 2 - Default Argument Values (Parallel Resistance Calculation)
# ==============================================================================
# Create a function to calculate parallel resistance with a default value for r2.

def parallel_resistance(r1, r2=100.0):
    req = (r1 * r2) / (r1 + r2)
    return req

# Using default value for r2 (100 ohms)
res1 = parallel_resistance(50.0)
print("Equivalent Resistance (Default r2=100):", res1, "ohms")

# Providing custom value for r2
res2 = parallel_resistance(50.0, 200.0)
print("Equivalent Resistance (Custom r2=200):", res2, "ohms")


# ==============================================================================
# Task 3 - Arbitrary Arguments (*args) (Total Power Consumption)
# ==============================================================================
# Calculate total power load from multiple electrical appliances.

def total_power_consumption(*powers):
    total = 0.0
    for p in powers:
        total += p
    return total

p_home = total_power_consumption(60.5, 120.0, 15.0)
print("Total Power (3 loads):", p_home, "W")

p_lab = total_power_consumption(100.0, 250.0, 75.0, 500.0, 12.5)
print("Total Power (5 loads):", p_lab, "W")


# ==============================================================================
# Task 4 - Arbitrary Keyword Arguments (**kwargs) (Component Specifications)
# ==============================================================================
# Print specs of electrical components dynamically using **kwargs.

def print_component_specs(**specs):
    print("--- Component Specification Sheet ---")
    for key, value in specs.items():
        print(key, ":", value)

print_component_specs(name="Resistor", value="10k ohm", tolerance="5%", power_rating="0.25W")
print_component_specs(name="Capacitor", capacitance="100uF", max_voltage="25V")


# ==============================================================================
# Task 5 - Recursion (Series Resistor Network Reduction)
# ==============================================================================
# Recursively sum series resistors without using built-in sum().

def sum_series_resistors(r_list):
    if not r_list:
        return 0
    return r_list[0] + sum_series_resistors(r_list[1:])

resistors = [120, 330, 470, 1000]
total_r = sum_series_resistors(resistors)
print("Resistor list:", resistors)
print("Total Series Resistance (Recursive):", total_r, "ohms")


# ==============================================================================
# Task 6 - Math Module (AC Circuit Impedance & Phase Angle)
# ==============================================================================
# Calculate impedance magnitude and phase angle of an RLC circuit.

import math

def calculate_impedance(r, x_l, x_c):
    x_net = x_l - x_c
    z = math.sqrt(r**2 + x_net**2)
    
    angle_rad = math.atan2(x_net, r)
    angle_deg = math.degrees(angle_rad)
    
    return z, angle_deg

imp, phase = calculate_impedance(100.0, 250.0, 100.0)
print("Impedance Magnitude (Z):", round(imp, 2), "ohms")
print("Phase Angle:", round(phase, 2), "degrees")


# ==============================================================================
# Task 7 - List Methods: append(), insert(), and remove()
# ==============================================================================
# Manage sensor readings using basic list operations.

readings = [4.9, 5.0, 5.1]
print("Initial Readings:", readings)

readings.append(5.05)
print("After append(5.05):", readings)

readings.insert(1, 4.95)
print("After insert at index 1:", readings)

readings.remove(5.1)
print("After removing 5.1:", readings)


# ==============================================================================
# Task 8 - List Methods: pop(), index(), and count()
# ==============================================================================
# Analyze digital logic gate signals using list methods.

logic_states = [1, 0, 1, 1, 0, 0, 1, 1]

high_count = logic_states.count(1)
print("HIGH state count:", high_count)

first_zero = logic_states.index(0)
print("First LOW state at index:", first_zero)

last_state = logic_states.pop()
print("Popped last state:", last_state)
print("Updated logic states:", logic_states)


# ==============================================================================
# Task 9 - Manual Sorting without sorted() (Signal Noise Sorting)
# ==============================================================================
# Sort noise amplitudes in ascending order using bubble sort algorithm.

def sort_signals(signals):
    arr = list(signals)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

noise_levels = [0.45, 0.12, 0.89, 0.03, 0.27]
sorted_noise = sort_signals(noise_levels)
print("Raw Noise Levels:", noise_levels)
print("Sorted Noise Levels:", sorted_noise)


# ==============================================================================
# Task 10 - Manual Filtering without filter() (Over-voltage Detection)
# ==============================================================================
# Extract voltage readings higher than safety threshold.

def filter_overvoltage(voltages, max_limit):
    over_limit = []
    for v in voltages:
        if v > max_limit:
            over_limit.append(v)
    return over_limit

sensor_data = [220.5, 245.0, 218.0, 260.2, 230.0, 252.1]
threshold = 240.0

faults = filter_overvoltage(sensor_data, threshold)
print("Sensor Voltage Logs:", sensor_data)
print("Threshold Limit:", threshold, "V")
print("Over-voltage Fault Logs:", faults)