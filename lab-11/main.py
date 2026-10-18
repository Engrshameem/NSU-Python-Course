# NSU Python  Lab-11


# Task 1 — List from Iterator made and next()Task 1 — List from Iterator made and next()

print("Task 1")

voltages = [5, 10, 15, 20]

voltage_iterator = iter(voltages)

print(next(voltage_iterator))
print(next(voltage_iterator))
print(next(voltage_iterator))
print(next(voltage_iterator))


# Task 2 — Iterator Exhaustion ও StopIteration

print("Task 2")

current_values = [2, 4, 6]

value_iterator = iter(current_values)

print(next(value_iterator))
print(next(value_iterator))
print(next(value_iterator))

try:
    print(next(value_iterator))
except StopIteration:
    print("No more values available")

# Task 3 — for Loop how to Iterator use

print("Task 3")

temperature = [25, 30, 35, 40]

temperature_iterator = iter(temperature)

while True:
    try:
        value = next(temperature_iterator)
        print("Temperature:", value)
    except StopIteration:
        break

# Task 4 — Custom Iterator Class

print("Task 4")

class VoltageRange:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration

        value = self.current
        self.current += 5
        return value


voltages = VoltageRange(5, 20)

for voltage in voltages:
    print(voltage)


# Task 5 — Generator Function and yield

print("Task 5")

def generate_resistance(start, stop):
    while start <= stop:
        yield start
        start += 10


resistance = generate_resistance(10, 40)

for value in resistance:
    print("Resistance:", value, "Ohm")


# Task 6 — Generator-এর Lazy Evaluation

print("Task 6")

def power_generator(limit):
    for number in range(1, limit + 1):
        yield number ** 2


generator = power_generator(1000000)

print(next(generator))
print(next(generator))
print(next(generator))


# Task 7 — Generator Expression by Sensor Data Filter

print("Task 7")

sensor_data = [12, 18, 25, 31, 40, 45]

high_temperature = (
    value for value in sensor_data
    if value > 30
)

print(list(high_temperature))


# Task 8 — Function as an Argument

print("Task 8")

def calculate_power(voltage, current):
    return voltage * current


def calculate(func, voltage, current):
    return func(voltage, current)


power = calculate(calculate_power, 12, 5)

print("Power:", power, "W")


# Task 9 — Closure

print("Task 9")

def create_converter(factor):
    def convert(value):
        return value * factor

    return convert


kw_to_watt = create_converter(1000)
mw_to_watt = create_converter(1000000)

print(kw_to_watt(2))
print(mw_to_watt(3))


# Task 10 — Decorator with *args, **kwargs and wraps

print("Task 10")

from functools import wraps


def log_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running:", func.__name__)
        result = func(*args, **kwargs)
        print("Operation completed")
        return result

    return wrapper


@log_operation
def calculate_energy(voltage, current, time=1):
    return voltage * current * time


energy = calculate_energy(10, current=2, time=3)

print("Energy:", energy, "J")
print("Function name:", calculate_energy.__name__)


