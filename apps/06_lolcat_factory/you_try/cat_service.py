import os
import shutil
from pip._vendor import requests


def get_data_from_url(url):
    # make the request to the url, but we need to get it in stream (binary) mode, not text mode
    response = requests.get(url, stream=True)
    # return the raw result of the request aka the binary
    return response.raw


def save_image(folder, name, data):
    filename = os.path.join(folder, name + '.jpg')
    # 'wb' flag means write binary
    with open(filename, 'wb') as fileout:
        # shell util copies binary data from our download to the output file
        shutil.copyfileobj(data, fileout)


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)
