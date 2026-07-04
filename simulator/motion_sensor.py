import random


def generate_motion():
    return random.choices(
        ["detection", "no motion"],
        weights=[20, 80]
    )[0]