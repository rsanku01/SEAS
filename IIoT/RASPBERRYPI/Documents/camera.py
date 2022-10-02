from sense_hat import SenseHat
from time import sleep
from datetime import datetime
from picamera import PiCamera

sense = SenseHat()
camera = PiCamera()
camera.rotation = 180

while True:
    event = sense.stick.wait_for_event()
    while event:
        direction = event.direction

        if direction == "middle":
            camera.start_preview()
            # sleep(3)
            camera.capture("image" + str(datetime.now()) + ".jpg")
            # sleep(2)
            # camera.stop_preview()
            # camera.close()

            break

        break
