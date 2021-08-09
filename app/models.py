class newsSource:
    '''
    Generate the news in from a a country
    '''

    def __init__(self,title,name,author,urlToImage,description,url,publishedAt):
        '''
        Initiate the news source class blueprint

        args: 
            title = title of the news
            name = station thats hosting the news article
            author = person that wrote the article
            description = full details on that specific title
        '''
        self.title = title
        self.name = name
        self.author = author
        self.urlToImage = urlToImage
        self.description = description
        self.url = url
        self.publishedAt = publishedAt


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