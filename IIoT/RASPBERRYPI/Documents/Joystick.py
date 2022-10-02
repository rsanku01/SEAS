from sense_hat import SenseHat
from time import sleep

# from signal import pause
from datetime import datetime


sense = SenseHat()
sense.clear()
event = sense.stick.wait_for_event()

while True:
    event = sense.stick.wait_for_event()
    while event:
        direction = event.direction

        if direction == "left":
            sense.show_message("left", text_colour=[255, 0, 0])
            sleep(1)

        elif direction == "right":
            sense.show_message("right", text_colour=[0, 255, 0])
            sleep(1)

        elif direction == "up":
            sense.show_message("Up", text_colour=[0, 0, 255])
            sleep(0.5)

        elif direction == "down":
            sense.show_message("Down", text_colour=[255, 0, 255])
            sleep(1)

        else:
            sense.show_message("Middle", text_colour=[127, 127, 127])
            sleep(1)

        break
    sense.clear()
