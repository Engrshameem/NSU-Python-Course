# NSU Python - Lab 06
# Practice Topics: Function are Object, Function as an Argument, Lamda Expretion, 
                #  Sorted(), Short() vs Shorted()Desending Order, Key Parameters, 
                #  Case Insentive Shorting, Shorting Tuples,Filtering Values, 
                #  Filter()+lambda, Map(), Iterator+list, 


# Complite Tasks 1-15.
# Use only concepts covered in Lecture 05 and earlier lecture.



# Task 1 - Function are Object

print("Task-1")

def calculate_power(voltage, current):
    power = voltage * current
    return power

power_function = calculate_power

result = power_function(220, 5)

print("Voltage:", 220, "V")
print("Current:", 5, "A")
print("Electrical Power:", result, "W") 

# Task 02 

print("Task-2")


def calculate_power(voltage, current):
    return voltage * current

def display_power(function, voltage, current):
    result = function(voltage, current)
    print("Electrical Power:", result, "W")

display_power(calculate_power, 230, 4)

# Task 03

print("Task-3")


voltage = 120
current = 4

calculate_resistance = lambda v, i: v / i

resistance = calculate_resistance(voltage, current)

print("Voltage:", voltage, "V")
print("Current:", current, "A")
print("Resistance:", resistance, "Ohm")

# Task 04

print("Task-4")


voltages = [220, 12, 110, 24, 5, 48]

sorted_voltages = sorted(voltages)

print("Original Voltages:", voltages)
print("Sorted Voltages:", sorted_voltages)

# Task 05

print("Task-5")



currents = [10, 2, 8, 5, 15]

new_currents = sorted(currents)

print("Original List:", currents)
print("Using sorted():", new_currents)

currents.sort()

print("Using sort():", currents)

# Task 06

print("Task-6")

currents = [5, 12, 3, 20, 8]

descending_currents = sorted(currents, reverse=True)

print("Current Values:", currents)
print("Descending Order:", descending_currents)

# Task 07

print("Task-7")



resistors = [
    ("R1", 100),
    ("R2", 10),
    ("R3", 220),
    ("R4", 47)
]

sorted_resistors = sorted(
    resistors,
    key=lambda x: x[1]
)

print("Sorted Resistors:")

for resistor in sorted_resistors:
    print(resistor)

    # Task 08

print("Task-8")


components = [
    "Resistor",
    "capacitor",
    "TRANSISTOR",
    "diode",
    "Inductor"
]

sorted_components = sorted(
    components,
    key=str.lower
)

print("Case-Insensitive Sorted List:")

for component in sorted_components:
    print(component)

    # Task 09

print("Task-9")


students = [
    ("Rahim", 75),
    ("Karim", 88),
    ("Hasan", 65),
    ("Sakib", 92)
]

sorted_students = sorted(
    students,
    key=lambda x: x[1],
    reverse=True
)

print("Students Sorted by Marks:")

for student in sorted_students:
    print(student)

    # Task 10

print("Task-10")


voltages = [5, 12, 24, 48, 110, 220, 240]

high_voltages = []

for voltage in voltages:
    if voltage >= 100:
        high_voltages.append(voltage)

print("Original Voltages:", voltages)
print("High Voltages:", high_voltages)

# Task 11

print("Task-11")


voltages = [5, 12, 24, 48, 110, 220, 240]

high_voltages = list(
    filter(lambda voltage: voltage >= 100, voltages)
)

print("Original Voltages:", voltages)
print("Filtered Voltages:", high_voltages)

# Task 12

print("Task-12")


voltages = [5, 10, 15, 20]

double_voltages = list(
    map(lambda voltage: voltage * 2, voltages)
)

print("Original Voltages:", voltages)
print("Doubled Voltages:", double_voltages)

# Task 13

print("Task-13")


components = [
    "Resistor",
    "Capacitor",
    "Diode",
    "Transistor"
]

component_iterator = iter(components)

print(next(component_iterator))
print(next(component_iterator))
print(next(component_iterator))
print(next(component_iterator))


# Task 14

print("Task-14")


components = [
    "Resistor",
    "Capacitor",
    "Diode",
    "Transistor"
]

component_iterator = iter(components)

for component in component_iterator:
    print("Electronic Component:", component)

# Task 15

print("Task-14")


components = [
    ("Resistor", 100),
    ("Capacitor", 20),
    ("Transistor", 50),
    ("Diode", 10),
    ("Inductor", 80)
]

def double_value(component):
    return component[1] * 2

filtered_components = filter(
    lambda x: x[1] >= 50,
    components
)

transformed_values = map(
    double_value,
    filtered_components
)

result = sorted(
    transformed_values,
    reverse=True
)

print("Final Sorted Values:", result)