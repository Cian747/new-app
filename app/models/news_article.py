class newsArticle:
    '''
    Fetch news data in articles
    '''

    def __init__(self,name,description,language,category,url,country):
        '''
        fetching the necessary data to display the info in an article.

        Args:
            language = language of the news
            category = picks the type of category ie. Business,Sports,Health
            name = name of the station or site hosting
            url = link to the page that's sources the news
        '''
        self.name = name
        self.description = description
        self.language = language
        self.category = category
        self.url = url
        self.country = country