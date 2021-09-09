import datetime
import os
import requests


from extension_handler import get_extension
from image_downloader import get_image


def fetch_nasa_apod(images_folder, token):
    response = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key={}&count=10'
        .format(token))
    response.raise_for_status()
    launches_data = response.json()
    launch_images = []

    for launch in launches_data:
        launch_images.append(launch['url'])

    for image_number, image_url in enumerate(launch_images, start=1):
        image_name = 'nasa{}{}'.format(
            image_number,
            get_extension(image_url))
        filepath = os.path.join(images_folder, image_name)

        get_image(image_url, filepath)


def fetch_nasa_epic(images_folder, token):
    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images?api_key={}'
        .format(token))
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
            token)
        image_name = 'epic{}.png'.format(image_number)
        filepath = os.path.join(images_folder, image_name)

        get_image(image_url, filepath)
