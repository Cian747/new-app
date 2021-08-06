class newsSource:
    '''
    Generate the news in from a a country
    '''

    def __init__(self,title,station,author,description):
        '''
        Initiate the news source class blueprint

        args: 
            title = title of the news
            station = station thats hosting the news article
            author = person that wrote the article
            description = full details on that specific title
        '''
        self.title = title
        self.station = station
        self.author = author
        self.description = description
