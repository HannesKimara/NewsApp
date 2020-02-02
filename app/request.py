import requests
from .models import Source

API_KEY, BASE_URL, SOURCE_API_URL = None, None, None

def configure_request(app):
    """
    Function that sets up constants required for requests
    """
    global API_KEY, BASE_URL, SOURCE_API_URL
    API_KEY = app.config['NEWS_API_KEY']
    BASE_URL = app.config['NEWS_API_BASE_URL']
    SOURCE_API_URL = BASE_URL + "sources"

def get_sources():
    """
    Function that gets sources from News Api
    """
    response = requests.get(SOURCE_API_URL, params = {"apiKey": API_KEY})

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return False

def process_sources(data):
    """
    Function that processes sources from get_sources
    """
    all_sources = []

    for src in data['sources']:
        new_source = Source(src['id'], src['name'], src['description'], src['category'], src['language'], src['country'])
        all_sources.append(new_source)

    return all_sources
