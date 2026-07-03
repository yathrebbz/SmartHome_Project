import random

def generate_temperature():
    temperature = round(random.uniform(20,35),1)
    return temperature
print(generate_temperature())