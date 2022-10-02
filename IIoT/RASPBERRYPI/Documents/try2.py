from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()


def orientation():
    bearing = sense.get_compass()
    print(f"Intial Bearing is {bearing:.1f}")
    sleep(2)
    return bearing


def changed_orientation(bearing):

    while True:
        bearing_1 = sense.get_compass()
        if bearing_1 >= 1.2 * bearing or bearing >= 1.2 * bearing:

            print(f"New Bearing is {bearing_1:.1f}")
            sense.show_message("left", text_colour=[255, 0, 0])
            break

        else:
            print("Nothing Changed is", bearing_1)
            sleep(1)
            continue


def main():

    while True:
        bearing = orientation()
        sleep(1)
        changed_orientation(bearing)
        sleep(1)


if __name__ == "__main__":
    main()
