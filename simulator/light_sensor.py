import random

hour = 8


def generate_light():
    global hour

    if 6 <= hour <= 18:
        light = random.randint(400, 1000)
    else:
        light = random.randint(0, 80)

    hour += 1

    if hour > 23:
        hour = 0

    return light