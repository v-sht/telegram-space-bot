import os
import requests

from urllib.parse import urlparse


def get_extension(url):
    path = urlsplit(url).path
    extension = unquote(Path(path).suffix)
    return extension


def get_image(url, filepath):
    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)
