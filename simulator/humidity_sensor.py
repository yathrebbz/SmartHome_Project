import random

humidity = 60


def generate_humidity():
    global humidity

    variation = random.randint(-2, 2)

    humidity += variation

    humidity = max(40, min(80, humidity))

    return humidity