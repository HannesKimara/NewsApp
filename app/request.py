import requests
from .models import Source, Article

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

def get_articles(endpoint, query_params):
    """
    Function that queries articles from newsapi
    """
    query_params["apiKey"] = API_KEY
    response = requests.get(BASE_URL+endpoint, params=query_params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return False

def process_articles(data):
    """
    Function that processes articles from get_articles
    """

    all_articles = []

    for art in data['articles']:
        if art['urlToImage'] != "null" and art['urlToImage'] != None :
            new_article = Article(art['author'], art['title'], art['url'], art['urlToImage'], art['description'], art['publishedAt'])
            all_articles.append(new_article)
        else:
            pass
    
    return all_articles