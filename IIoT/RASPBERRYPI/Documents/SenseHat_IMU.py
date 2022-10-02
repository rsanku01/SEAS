from sense_hat import SenseHat
from time import sleep
from datetime import datetime

sense = SenseHat()
# sense.set_imu_config(False, True, True)  # (compass,gyroscope,accelerometer)


orientation = sense.get_orientation()
accel_only = sense.get_accelerometer()
raw = sense.get_gyroscope_raw()
while True:
    # print(orientation)
    # sleep(2)

    print(abs(sense.orientation))
    sleep(2)
    print(sense.get_compass())
    sleep(2)
print("r: {roll}, p: {pitch}, y: {yaw}".format(**orientation))
sleep(1)
# print(sense.orientation)
print(sense.get_compass())
# sleep(1)
# print(accel_only)
sleep(1)
# print(raw)
# sleep(1)
# print(sense.gyro)
# sleep(1)
# print(sense.gyroscope)
# sleep(1)
