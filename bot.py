import os
import telegram
import time
from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic
from fetch_spacex import fetch_spacex_last_launch
from dotenv import load_dotenv


def main():
    load_dotenv()
    fetch_spacex_last_launch()
    fetch_nasa_apod()
    fetch_nasa_epic()

    bot = telegram.Bot(token=os.environ['TG_TOKEN'])
    images = os.listdir('images')

    while True:
        for image in images:
            bot.send_photo(
                chat_id=os.environ['CHAT_ID'],
                photo=open('images/{}'.format(image), 'rb'))
            time.sleep(10)


if __name__ == '__main__':
    main()
