from instance.config import NEWS_API_KEY
from app import app
from .models import news_source
import urllib.request,json
from .models import news_article

Find = news_article.newsArticle

News = news_source.newsSource

# Fetching the api_key
api_key = NEWS_API_KEY

# fetch the new source url
news_source_url = app.config['NEWS_API_SOURCE_URL']

news_category_url = app.config['NEWS_API_CATEGORY_URL']

news_channel_url = app.config['NEWS_API_CHANNEL_URL']

news_search_url = app.config['NEWS_API_SEARCH_URL']


def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = news_source_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        date_pick = news_item.get('publishedAt')
        image = news_item.get('urlToImage')
        station = news_item.get('name')
        source = news_item.get('url')

    # if image:
        article_object = News(title,station,author,image,description,source,date_pick)
        news_results.append(article_object)

    return news_results

def search_category(category):
    '''
    Function to get the categories
    '''
    get_search_url = news_category_url.format(category,api_key)

    with urllib.request.urlopen(get_search_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results= category_results(news_results_list)


    return news_results



def category_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_category_results = []
    for news_item in news_list:
        name = news_item.get('name')
        description = news_item.get('description')
        category = news_item.get('category')
        language = news_item.get('language')
        source = news_item.get('url')
        country = news_item.get('country')

    # if :
        category_object = Find(name,description,language,category,source,country)
        news_category_results.append(category_object)

    return news_category_results


def get_channel(channel_id):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = news_channel_url.format(channel_id,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def get_query(query):
    '''
    Function that gets the json response to our url request
    '''
    get_query_url = news_search_url.format(query,api_key)

    with urllib.request.urlopen(get_query_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results