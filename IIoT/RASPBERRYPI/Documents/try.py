from sense_hat import SenseHat
from picamera import PiCamera
import os
from telethon.sync import TelegramClient, events
from time import sleep
from datetime import datetime

sense = SenseHat()
camera = PiCamera()
for i in range(6):
    if i >= 0 & i <= 3:
        sense.clear(255, 0, 0)
        sense.low_light = True
        sleep(0.5)
        sense.clear(255, 255, 255)
        sense.low_light = True
        sleep(0.5)

    elif i > 3 & i <= 6:
        sense.clear(255, 0, 0)
        sense.low_light = True
        sleep(0.5)
        sense.clear(255, 255, 255)
        sense.low_light = True
        sleep(0.5)

for _ in range(3):
    camera.capture("image" + str(datetime.now()) + ".jpg")
    sleep(1)
