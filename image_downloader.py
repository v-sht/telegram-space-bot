import requests


def download_image(url, filepath, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)
