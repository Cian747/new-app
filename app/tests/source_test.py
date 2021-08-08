import unittest
from ..models import news_source,news_article


class testSource(unittest.TestCase):
    '''
    Tests article test and source classes
    '''

    def setUp(self):
        '''
        Initiallizing classes from both modules
        '''

        self.news_source = news_source.newsSource("ABC-News","abc-news",'https://image.tmdb.org/t/p/w500/khsjha27hbs',"latest news on abc","https://www.w3schools.com/html/default.asp","2021-12-03")
        self.news_article = news_article.newsArticle("Cian","News article is great","english","business","https://www.w3schools.com/html/default.asp","US")

    
    def test__init__(self):
        '''
        Testing the news source and news article class
        '''

        self.assertTrue(isinstance(self.news_source,news_source.newsSource))
        self.assertTrue(isinstance(self.news_article,news_article.newsArticle))

if __name__ == '__main__':
    unittest.main()