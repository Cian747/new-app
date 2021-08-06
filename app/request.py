from instance.config import NEWS_API_KEY
from app import app
from .models import news_source
import urllib.request,json
from .models import news_article

search = news_article.newsArticle

News = news_source.newsSource

# Fetching the api_key
api_key = NEWS_API_KEY

# fetch the new source url
news_source_url = app.config['NEWS_API_SOURCE_URL']

news_category_url = app.config['NEWS_API_CATEGORY_URL']


def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = news_source_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results


def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
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

        article_object = News(title,station,author,description)
        news_results.append(article_object)

    if image:
        category_object = search(id,image,date_pick,source)
        news_results.append(category_object)

    return news_results

def search_category(category):
    '''
    Function to get the categories
    '''
    get_search_url = news_category_url.format(category,api_key)

    with urllib.request.urlopen(get_search_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        # news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results
