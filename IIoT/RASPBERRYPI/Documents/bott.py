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


def send_photo(bot):

    for _ in range(3):
        time = str(datetime.now())
        camera.capture("image" + time + ".jpg")
        bot.send_file("@richie_anku", ("image" + time + ".jpg"))
        sleep(1)


def main():
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


if __name__ == "__main__":
    main()
