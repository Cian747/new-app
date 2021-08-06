class newsArticle:
    '''
    Fetch news data in articles

    Args:
        
    '''

    def __init__(self,id,urlToImage,description,publishedAt,url):
        '''
        fetching the necessary data to display the info in an article.

        Args:
            self.urlToImage = urlToImage
            self.publishedAt = publishedAt
            self.name = name
        '''
        self.id = id
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt
        self.url = url