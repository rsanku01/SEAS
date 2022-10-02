from sense_hat import SenseHat
from time import sleep
from datetime import datetime

sense = SenseHat()
sense.set_imu_config(False, True, False)  # (compass,gyroscope,accelerometer)
print(sense.set_imu_config(False, True, False))

while True:
    sense = SenseHat()
    humidity = sense.get_humidity()
    temp = sense.get_temperature()
    temp1 = sense.get_temperature_from_humidity()
    pressure = sense.get_pressure()

    print("Humidity: %s %%rH" % "{:.2f}".format(humidity))
    sleep(1)
    print("Temperature:%s °C" % "{:.2f}".format(temp))
    sleep(1)
    print("Temperature:%s °C" % "{:.2f}".format(temp1))
    sleep(1)
    print("Pressure: %s Millibars" % pressure)
    sleep(1)
