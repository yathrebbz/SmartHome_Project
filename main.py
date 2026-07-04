from simulator.temperature_sensor import generate_temperature
from simulator.humidity_sensor import generate_humidity
from simulator.light_sensor import generate_light
from simulator.motion_sensor import generate_motion
from datetime import datetime
import time
def main():

    while True:

        temperature = generate_temperature()
        humidity = generate_humidity()
        light = generate_light()
        motion = generate_motion()

        current_time = datetime.now()

        print("=" * 50)
        print("SMART HOME SIMULATOR")
        print("=" * 50)

        print("Time :", current_time.strftime("%H:%M:%S"))
        print("Date :", current_time.strftime("%d:/%m:/%Y"))
        print(f"🌡 Temperature : {temperature} °C")
        print(f"💧 Humidity    : {humidity} %")
        print(f"💡 Light       : {light} lux")
        print(f"🚶 Motion      : {motion}")

        if temperature > 30:
            print("🔥 High Temperature")

        if humidity > 70:
            print("💧 High Humidity")

        if light < 100:
            print("🌙 Low Light")

        if motion:
            print("🚨 Motion Detected")

        print()

        time.sleep(2) #Le programme attend 2 secondes avant de générer une nouvelle mesure.

#Sans cela, les données défileraient beaucoup trop vite.
        print()

        time.sleep(2)


if __name__ == "__main__":
    main()