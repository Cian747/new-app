from app.request import get_source, search_category
from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Nairobi Times'
    sources = get_source()
    return render_template('index.html', title = title, sources_news = sources)

@app.route('/category')
def search():
    '''
    Find the article category and redirect
    '''
    business = search_category('business')
    sports = search_category('sport')
    entertainment = search_category('entertainment')

    return render_template('search-news.html', business_news = business, ent_results = entertainment, sport_news = sports)


@app.route('/entertainment')
def entertainment():
    '''
    See all entertainment related news
    '''
    entertainment = search_category('entertainment')

    return render_template('index.html', entertainment = entertainment)


@app.route('/sports')
def sports():
    '''
    See all sports related news
    '''
    sports = search_category('sports')

    return render_template('index.html', sports = sports)


@app.route('/health')
def health():
    '''
    See all sports related news
    '''
    health = search_category('health')

    return render_template('index.html', health = health)

@app.route('/business')
def business():
    '''
    See all sports related news
    '''
    business = search_category('business')

    return render_template('index.html', business = business)

@app.route('/technology')
def tech():
    '''
    See all sports related news
    '''
    technology = search_category('technology')

    return render_template('index.html', technology = technology)


@app.route('/general')
def health():
    '''
    See all sports related news
    '''
    general = search_category('general')

    return render_template('sources.html', general = general)
