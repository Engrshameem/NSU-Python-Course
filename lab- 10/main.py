#NSU Python Lab-10


# Task- 1  Instance Attribute
# Problem: Create an ElectricalStudent class that stores each student's name and department.

print("Task 1")

class ElectricalStudent:
    def __init__(self, name, department):
        self.name = name
        self.department = department

student1 = ElectricalStudent("Rahim", "EEE")
student2 = ElectricalStudent("Karim", "EEE")

print(student1.name)
print(student1.department)

print(student2.name)
print(student2.department)


# Task- 2  Class Attribute
# Problem: Store a common university name that is shared by all students.

print("Task 2")

class Student:
    university = "Novosibirsk State University"

    def __init__(self, name):
        self.name = name

student1 = Student("Hasan")
student2 = Student("Sakib")

print(student1.name)
print(student1.university)

print(student2.name)
print(student2.university)


# Task 3: Encapsulation and Validation
# Problem: Create a battery class where voltage must remain between 0 and 24 volts.

print("Task 3")

class Battery:
    def __init__(self, voltage):
        self._voltage = 0
        self.set_voltage(voltage)

    def set_voltage(self, voltage):
        if 0 <= voltage <= 24:
            self._voltage = voltage
        else:
            raise ValueError("Voltage must be between 0 and 24 volts.")

    def get_voltage(self):
        return self._voltage


battery = Battery(12)

print("Battery Voltage:", battery.get_voltage())

try:
    battery.set_voltage(30)
except ValueError as error:
    print("Error:", error)

print("Final Voltage:", battery.get_voltage())


# Task 4: Double Underscore
# Problem: Store a motor's current internally using a double underscore.

ptint("Task 4")

class Motor:
    def __init__(self, current):
        self.__current = current

    def get_current(self):
        return self.__current


motor = Motor(5)

print("Motor Current:", motor.get_current())


# Task 5: Exception Handling with Class
# Problem: Create a sensor class that accepts temperature only between -40°C and 125°C.

print("Task 5")

class TemperatureSensor:
    def __init__(self):
        self._temperature = None

    def set_temperature(self, temperature):
        if -40 <= temperature <= 125:
            self._temperature = temperature
        else:
            raise ValueError("Invalid temperature range.")

    def get_temperature(self):
        return self._temperature


sensor = TemperatureSensor()

try:
    sensor.set_temperature(35)
    print("Temperature:", sensor.get_temperature())

    sensor.set_temperature(150)

except ValueError as error:
    print("Error:", error)


# Task 6: Inheritance
# Problem: Create a base class Device and inherit it into Motor.

print("Task 6")

class Device:
    def __init__(self, name):
        self.name = name

    def information(self):
        return f"Device: {self.name}"


class Motor(Device):
    pass


motor = Motor("Induction Motor")

print(motor.name)
print(motor.information())


# Task 7: super() Function
# Problem: Create an Engineer class that inherits from Person.

print("Task 7")

class Person:
    def __init__(self, name):
        self.name = name


class Engineer(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def show_info(self):
        return f"{self.name} - {self.department}"


engineer = Engineer("Shameem", "Electrical Engineering")

print(engineer.show_info())

#  Task 8: Method Overriding
# Problem: Different devices should provide different descriptions.

print("Task 8")

class Device:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is an electrical device."


class Motor(Device):
    def describe(self):
        return f"{self.name} converts electrical energy into mechanical energy."


class Transformer(Device):
    def describe(self):
        return f"{self.name} changes AC voltage level."


motor = Motor("Induction Motor")
transformer = Transformer("Power Transformer")

print(motor.describe())
print(transformer.describe())


# ask 9: Polymorphism and Duck Typing
# Problem: Calculate the output power of different electrical devices using the same method

print("Task 9")

class Motor:
    def power(self):
        return 1500


class Generator:
    def power(self):
        return 2000


class SolarPanel:
    def power(self):
        return 500


devices = [Motor(), Generator(), SolarPanel()]

for device in devices:
    print("Power:", device.power(), "W")


# Task 10: Composition
# Problem: Create a Laboratory that contains different electrical devices.

print("Task 10")

class Device:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Device: {self.name}"


class Laboratory:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def show_devices(self):
        for device in self.devices:
            print(device.describe())


lab = Laboratory("Electrical Engineering Lab")

motor = Device("AC Motor")
transformer = Device("Transformer")
sensor = Device("Temperature Sensor")

lab.add_device(motor)
lab.add_device(transformer)
lab.add_device(sensor)

print("Laboratory:", lab.name)
lab.show_devices()