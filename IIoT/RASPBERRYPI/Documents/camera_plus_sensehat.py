from sense_hat import SenseHat
from time import sleep
from datetime import datetime
from picamera import PiCamera

sense = SenseHat()
camera = PiCamera()
camera.rotation = 180


def button_triggered():

    event = sense.stick.wait_for_event(emptybuffer=True)  # emptybuffer=True
    direction = event.direction
    return event, direction


def camera_capture(event, direction):
    camera.start_preview()
    sleep(1)
    if direction == "left":

        camera.capture("image" + str(datetime.now()) + ".jpg")
        print("Image Captured")
        sleep(0.5)
        # direction = button_triggered()[1]
        while True:
            direction = button_triggered()[1]
            if direction == "middle":
                camera.stop_preview()
                print("Camera Stopped")
                sleep(2)
                break

            else:
                continue

    else:
        # event
        print("Waiting for Trigger")
        # event


def main():

    while True:
        event, direction = button_triggered()

        camera_capture(event, direction)


if __name__ == "__main__":
    main()
