import csv
import os

FILE_NAME = "data/sensor_data.csv"


def save_data(time, temperature, humidity, light, motion):

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Time",
                "Temperature",
                "Humidity",
                "Light",
                "Motion"
            ])

        writer.writerow([
            time,
            temperature,
            humidity,
            light,
            motion
        ])