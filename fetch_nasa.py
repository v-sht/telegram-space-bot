import datetime
import os
import requests

from dotenv import load_dotenv
from main import image_downloader, ensure_category, extension_parser


def fetch_nasa_apod():
    load_dotenv()
    response = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key={}&count=10'
        .format(os.environ['NASA_TOKEN']))
    response.raise_for_status()
    launches_data = response.json()
    launch_images = []

    for launch in launches_data:
        launch_images.append(launch['url'])

    for image_number, image_url in enumerate(launch_images, start=1):
        image_name = 'nasa{}{}'.format(
            image_number,
            extension_parser(image_url))
        folder_name = 'images'
        ensure_category(folder_name)
        filepath = os.path.join(folder_name, image_name)

        image_downloader(image_url, filepath)


def fetch_nasa_epic():
    load_dotenv()
    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images?api_key={}'
        .format(os.environ['NASA_TOKEN']))
    response.raise_for_status()
    photos_data = response.json()

    for image_number, photo_data in enumerate(photos_data, start=1):
        image_date = photo_data['date']
        image_date_datetime = datetime.datetime.fromisoformat(image_date)
        image_url = 'https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png?api_key={4}'.format(
            image_date_datetime.year,
            image_date_datetime.strftime('%m'),
            image_date_datetime.strftime('%d'),
            photo_data['image'],
            os.environ['NASA_TOKEN'])
        folder_name = 'images'
        ensure_category(folder_name)
        image_name = 'epic{}.png'.format(image_number)
        filepath = os.path.join(folder_name, image_name)

        image_downloader(image_url, filepath)
