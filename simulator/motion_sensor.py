import random


def generate_motion():
    return random.choices(
        [True, False],
        weights=[20, 80]
    )[0]