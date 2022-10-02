from sense_hat import SenseHat
from picamera import PiCamera

# import os
from telethon.sync import TelegramClient, events
from time import sleep
from datetime import datetime

sense = SenseHat()
camera = PiCamera()
sense.clear()
sense.set_imu_config(True, True, False)

camera.rotation = 180

# """"Send a message when the command /start is issued."""
async def start(event):
    """Send a message when the command /start is issued."""
    sender = await event.get_sender()
    await event.respond("Hi " + sender.first_name + "!")


# """Send Photo to Telegram Bot"""
def send_photo(bot):

    for _ in range(3):
        camera.capture("image" + ".jpg")  # + str(datetime.now())
        bot.send_file("@richie_anku", "image" + ".jpg")  # + str(datetime.now())


# """Get Orientation of Device"""
def orientation():
    bearing = sense.get_compass()
    print(f"Intial Bearing is {bearing:.1f}")
    sleep(2)
    return bearing


# """Alert and Alarm on SenseHat LED"""
def alert_alarm():
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
    sense.clear()


# """Start Telegram Bot"""
def start_bot():
    session = "IIoT Security"
    api_id = 19494202
    api_hash = "165576d3141d6084a2a787d3f58cdd8f"
    bot_token = "5744277943:AAETuDHudljTt5YrF27s1s8f5FSPZk3qVtc"
    bot = TelegramClient(session, api_id, api_hash)
    bot.add_event_handler(start, events.NewMessage(pattern="/start"))
    bot.start(bot_token=bot_token)
    bot.send_message("@richie_anku", "Hello Someone touched the device!")
    # alert_alarm()
    send_photo(bot)
    bot.run_until_disconnected()


# """Check for Change In Device Orientation"""
def if_orientation_change(bearing):
    return sense.get_compass()

    while True:
        bearing_1 = sense.get_compass()
        if bearing_1 >= 1.1 * bearing or bearing >= 1.1 * bearing_1:

            print(f"New Bearing is {bearing_1:.1f}")
            alert_alarm()
            start_bot()
            # sense.clear()
            break

        else:
            print(f"Nothing Changed is {bearing_1:.1f}")
            sleep(1)
            continue


def main():
    """Start the bot."""

    bearing = orientation()
    sleep(1)
    if_orientation_change(bearing)
    sleep(1)

    # session = "IIoT Security"
    # api_id = 19494202
    # api_hash = "165576d3141d6084a2a787d3f58cdd8f"
    # bot_token = "5744277943:AAETuDHudljTt5YrF27s1s8f5FSPZk3qVtc"
    # bot = TelegramClient(session, api_id, api_hash)
    # bot.add_event_handler(start, events.NewMessage(pattern="/start"))
    # bot.start(bot_token=bot_token)
    # bot.send_message("@richie_anku", "!")
    # alert_alarm()
    # send_photo(bot)
    # bot.run_until_disconnected()


if __name__ == "__main__":
    main()
