import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_CATEGORY_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'
    NEWS_API_CHANNEL_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEwS_API_KEY')

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}