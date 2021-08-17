import os
import requests

from urllib.parse import urlparse


def extension_parser(url):
    url_path = urlparse(url).path
    url_ext = os.path.splitext(url_path)
    return url_ext[1]


def ensure_category(folder_name):
    os.makedirs(folder_name, exist_ok=True)


def image_downloader(url, filepath):
    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)
