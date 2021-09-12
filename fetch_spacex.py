import os
import requests

from image_downloader import download_image


def fetch_spacex_launch(images_folder, launch_number):
    response = requests.get('https://api.spacexdata.com/v3/launches/{}'.format(launch_number))
    response.raise_for_status()
    launch_images = response.json()['links']['flickr_images']

    for image_number, image_url in enumerate(launch_images, start=1):
        image_name = 'space{}.jpg'.format(image_number)
        filepath = os.path.join(images_folder, image_name)

        download_image(image_url, filepath)
