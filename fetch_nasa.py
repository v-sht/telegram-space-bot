import datetime
import os
import requests

from extension_handler import get_extension
from image_downloader import download_image


def fetch_nasa_apod(images_folder, token):

    payload = {
        'api_key': token,
        'count': 3,
    }

    response = requests.get(
        'https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    launches = response.json()

    for image_number, launch in enumerate(launches, start=1):
        image_name = 'nasa{}{}'.format(
            image_number,
            get_extension(launch['url']))
        filepath = os.path.join(images_folder, image_name)

        download_image(launch['url'], filepath)


def fetch_nasa_epic(images_folder, token):

    payload = {
        'api_key': token,
    }

    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images', params=payload)
    response.raise_for_status()
    photos = response.json()

    for image_number, photo in enumerate(photos, start=1):
        image_date = photo['date']
        image_date_datetime = datetime.datetime.fromisoformat(image_date)

        image_url = 'https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png'.format(
            image_date_datetime.strftime('%Y/%m/%d'),
            photo['image'])
        image_name = 'epic{}.png'.format(image_number)
        filepath = os.path.join(images_folder, image_name)

        download_image(image_url, filepath, payload)
