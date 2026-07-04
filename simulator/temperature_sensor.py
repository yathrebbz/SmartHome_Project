import random

temperature = 25.0


def generate_temperature():
    global temperature

    variation = random.uniform(-0.3, 0.3)

    temperature = temperature + variation

    temperature = max(20, min(35, temperature))

    return round(temperature, 1)