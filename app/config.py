class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_CATEGORY_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'

    # https://newsapi.org/v2/top-headlines?country=us&apiKey=b9cac6e7bd5b4295aca46e319913d53b
    # https://newsapi.org/v2/top-headlines/sources?category=entertainementapiKey=b9cac6e7bd5b4295aca46e319913d53b'

    # SOURCES
    # BUSINESS
    # ENTERTAINMENT
    # SPORTS
    # HEALTH
    # SCIENCE




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