from datetime import datetime
import random


class Room:

    def __init__(self, name):
        self.name = name

    # -----------------------------
    # Daily Pattern
    # -----------------------------
    def get_daily_conditions(self):

        hour = datetime.now().hour

        if 0 <= hour < 6:
            return 20, 70, 50, 0.05

        elif 6 <= hour < 10:
            return 22, 65, 300, 0.40

        elif 10 <= hour < 17:
            return 27, 55, 700, 0.70

        elif 17 <= hour < 21:
            return 25, 60, 500, 0.90

        else:
            return 21, 65, 80, 0.10

    # -----------------------------
    # Temperature
    # -----------------------------
    def generate_temperature(self, base_temp):

        offsets = {
            "Living Room": 0,
            "Bedroom": -2,
            "Kitchen": 3
        }

        return round(
            base_temp +
            offsets[self.name] +
            random.uniform(-0.5, 0.5),
            1
        )

    # -----------------------------
    # Humidity
    # -----------------------------
    def generate_humidity(self, base_humidity):

        offsets = {
            "Living Room": 0,
            "Bedroom": 5,
            "Kitchen": 3
        }

        return base_humidity + offsets[self.name] + random.randint(-2, 2)

    # -----------------------------
    # Light
    # -----------------------------
    def generate_light(self, base_light):

        factors = {
            "Living Room": 1.0,
            "Bedroom": 0.3,
            "Kitchen": 1.2
        }

        return int(
            base_light *
            factors[self.name] +
            random.randint(-30, 30)
        )

    # -----------------------------
    # Motion
    # -----------------------------
    def generate_motion(self, probability):

        return random.random() < probability

    # -----------------------------
    # Read all sensors
    # -----------------------------
    def read_sensors(self):
        base_temp, base_humidity, base_light, probability = self.get_daily_conditions()
        probability = self.get_room_motion_probability()
        return {
            "Room": self.name,
            "Temperature": self.generate_temperature(base_temp),
            "Humidity": self.generate_humidity(base_humidity),
            "Light": self.generate_light(base_light),
            "Motion": self.generate_motion(probability)
        }

    def get_weekly_factor(self):
        
        weekday = datetime.now().weekday()

        if weekday <= 4:      # Lundi à Vendredi
            return 0.3
        elif weekday == 5:    # Samedi
            return 0.8
        else:                 # Dimanche
            return 1.0
def get_room_motion_probability(self):

    hour = datetime.now().hour
    weekday = datetime.now().weekday()

    if weekday <= 4 and 8 <= hour < 17:
        return 0.05

    if 6 <= hour < 8:
        probabilities = {
            "Kitchen": 0.90,
            "Living Room": 0.40,
            "Bedroom": 0.60
        }

    elif 17 <= hour < 22:
        probabilities = {
            "Kitchen": 0.50,
            "Living Room": 0.90,
            "Bedroom": 0.30
        }

    else:
        probabilities = {
            "Kitchen": 0.05,
            "Living Room": 0.10,
            "Bedroom": 0.20
        }

    return probabilities[self.name]