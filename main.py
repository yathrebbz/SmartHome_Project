from simulator.temperature_sensor import generate_temperature
from simulator.humidity_sensor import generate_humidity
from simulator.light_sensor import generate_light
from simulator.motion_sensor import generate_motion
from simulator.room import Room
from datetime import datetime
from data.data_logger import save_data
import time


def main():

    living_room = Room("Living Room")
    bedroom = Room("Bedroom")
    kitchen = Room("Kitchen")

    while True:

        rooms = [
            living_room.read_sensors(),
            bedroom.read_sensors(),
            kitchen.read_sensors()
        ]

        current_time = datetime.now()

        for room in rooms:

            save_data(
                current_time.strftime("%H:%M:%S"),
                room["Room"],
                room["Temperature"],
                room["Humidity"],
                room["Light"],
                room["Motion"]
            )

        print("=" * 60)
        print("SMART HOME SIMULATOR")
        print("=" * 60)

        print("Time :", current_time.strftime("%H:%M:%S"))
        print()

        for room in rooms:

            print(f"🏠 Room : {room['Room']}")
            print(f"🌡 Temperature : {room['Temperature']} °C")
            print(f"💧 Humidity    : {room['Humidity']} %")
            print(f"💡 Light       : {room['Light']} lux")
            print(f"🚶 Motion      : {room['Motion']}")

            if room["Temperature"] > 30:
                print("🔥 High Temperature")

            if room["Humidity"] > 70:
                print("💧 High Humidity")

            if room["Light"] < 100:
                print("🌙 Low Light")

            if room["Motion"]:
                print("🚨 Motion Detected")

            print("-" * 50)

        print()

        time.sleep(2)


if __name__ == "__main__":
    main()