# NSU Python - Lab 09


# Complite Tasks : 1-10
# Use only concepts covered in Lecture 09 and earlier lecture.



# Task - 1  Safe Voltage Input
# Topic: try, except, ValueError
print("Task-1")
  
voltage_text = input("Enter voltage: ")

try:
    voltage = float(voltage_text)
    print("Voltage =", voltage, "V")

except ValueError:
    print("Invalid voltage. Please enter a number.")

# Task - 2 Safe Electrical Power Calculation 
# Topic: Multiple, except, Zero Division Error, Value Error
print("Task-2")

try:
    voltage = float(input("Enter voltage (V): "))
    resistance = float(input("Enter resistance (ohm): "))

    current = voltage / resistance

except ValueError:
    print("Please enter numeric values.")

except ZeroDivisionError:
    print("Resistance cannot be zero.")

else:
    print("Current =", current, "A")


# Task- 3 Battery Voltage Validation
# Topic: raise, valueError

print("Task- 3")

def check_voltage(voltage):
    if voltage < 0:
        raise ValueError("Voltage cannot be negative.")

    if voltage > 500:
        raise ValueError("Voltage is outside the safe range.")

    return voltage


try:
    value = float(input("Enter battery voltage: "))
    print("Accepted voltage:", check_voltage(value), "V")

except ValueError as error:
    print("Error:", error)


# Task - 4 Temperature Input with finally
# Topic: try, except, finally

print("Task 4")

try:
    temperature = float(input("Enter temperature: "))

    if temperature > 100:
        print("High temperature detected.")
    else:
        print("Temperature is normal.")

except ValueError:
    print("Invalid temperature.")

finally:
    print("Temperature checking completed.")


# Task- 5
# Topic: Motor Speed Input with Retry

print("Task 5")

while True:
    try:
        speed = int(input("Enter motor speed: "))

        if speed < 0:
            print("Speed cannot be negative.")
            continue

        break

    except ValueError:
        print("Please enter a whole number.")

print("Accepted motor speed:", speed, "RPM")


# Task 6 Reading Sensor Daga from File
# Topic: file handling + FileNoFoundError + ValueError

print("Task 6")

try:
    with open("sensor.txt", "r", encoding="utf-8") as file:
        temperatures = [float(line.strip()) for line in file]

except FileNotFoundError:
    print("sensor.txt file was not found.")

except ValueError:
    print("The file contains invalid data.")

else:
    average = sum(temperatures) / len(temperatures)
    print("Average temperature:", average)


# Task 7 Electrical Load Class
# Topic: Class, object, __init__, attributes

print("Task 7")

class ElectricalLoad:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def display(self):
        print("Load Name:", self.name)
        print("Power:", self.power, "W")


fan = ElectricalLoad("Ceiling Fan", 80)
lamp = ElectricalLoad("LED Lamp", 20)

fan.display()
lamp.display()


# Task- 8 Student Result Class
# Topic: Object, attributes, methods, self

print("Task 8")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Student:", self.name)
        print("Average:", self.average())


student1 = Student("Rahim", [75, 80, 85])
student2 = Student("Karim", [65, 70, 75])

student1.display()
student2.display()


# Task- 9 Motor Class with Validation
# Topic: Class + method + raise + exception handling

print("Task 9")

class Motor:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def set_speed(self, speed):
        if speed < 0 or speed > 3000:
            raise ValueError("Speed must be between 0 and 3000 RPM.")

        self.speed = speed

    def display(self):
        print("Motor:", self.name)
        print("Speed:", self.speed, "RPM")


motor = Motor("Induction Motor")

try:
    speed = int(input("Enter motor speed: "))
    motor.set_speed(speed)
    motor.display()

except ValueError as error:
    print("Error:", error)


    
