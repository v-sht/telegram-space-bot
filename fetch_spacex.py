import os
import requests

from main import image_downloader, ensure_category


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v3/launches/108')
    response.raise_for_status()
    launch_images = response.json()['links']['flickr_images']

    for image_number, image_url in enumerate(launch_images, start=1):
        image_name = 'space{}.jpg'.format(image_number)
        folder_name = 'images'
        ensure_category(folder_name)
        filepath = os.path.join(folder_name, image_name)

        image_downloader(image_url, filepath)
