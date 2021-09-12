import os
import telegram
import time

from dotenv import load_dotenv
from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic
from fetch_spacex import fetch_spacex_launch


def upload_images(images_folder, token, chat_id):
    bot = telegram.Bot(token=token)
    images = os.listdir(images_folder)
    while True:
        for image in images:
            with open('{0}/{1}'.format(images_folder, image), 'rb') as photo:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=photo)
            time.sleep(86400)    



def main():
    load_dotenv()
    images_folder = 'images'
    os.makedirs(images_folder, exist_ok=True)
    tg_token = os.environ['TG_TOKEN']
    nasa_token = os.environ['NASA_TOKEN']
    chat_id = os.environ['CHAT_ID']
    fetch_spacex_launch(images_folder, 108)
    fetch_nasa_apod(images_folder, nasa_token)
    fetch_nasa_epic(images_folder, nasa_token)
    upload_image(images_folder, tg_token, chat_id)


if __name__ == '__main__':
    main()
