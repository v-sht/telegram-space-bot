import os
import requests

from image_downloader import get_image


def fetch_spacex_last_launch(images_folder):
    response = requests.get('https://api.spacexdata.com/v3/launches/108')
    response.raise_for_status()
    launch_images = response.json()['links']['flickr_images']

    for image_number, image_url in enumerate(launch_images, start=1):
        image_name = 'space{}.jpg'.format(image_number)
        filepath = os.path.join(images_folder, image_name)

        get_image(image_url, filepath)
