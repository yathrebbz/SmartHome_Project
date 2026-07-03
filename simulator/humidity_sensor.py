import random

def generate_humidity():
    humidity = random.randint(40,80)
    return humidity

print(generate_humidity())