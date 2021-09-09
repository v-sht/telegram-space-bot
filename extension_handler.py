from pathlib import Path
from urllib.parse import unquote, urlsplit


def get_extension(url):
    path = urlsplit(url).path
    extension = unquote(Path(path).suffix)
    return extension
