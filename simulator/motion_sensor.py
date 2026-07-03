from simulator.temperature_sensor import generate_temperature
from simulator.humidity_sensor import generate_humidity
from simulator.light_sensor import generate_light
from simulator.motion_sensor import generate_motion

temperature = generate_temperature()
humidity = generate_humidity()
light = generate_light()
motion = generate_motion()

print("=" * 50)
print("SMART HOME SIMULATOR")
print("=" * 50)

print("Temperature :", temperature, "°C")
print("Humidity    :", humidity, "%")
print("Light       :", light, "lux")
print("Motion      :", motion)

print("=" * 50)