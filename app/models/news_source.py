class newsSource:
    '''
    Generate the news in from a a country
    '''

    def __init__(self,title,name,author,urlToImage,description,url):
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
