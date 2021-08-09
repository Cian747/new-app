from app.request import get_channel, get_query, get_source, search_category
from flask import render_template,request,redirect,url_for
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Nairobi Times'
    sources = get_source()

    search_result = request.args.get('search_query')

    if search_result:
        return redirect(url_for('main.search_results', input_name = search_result))
    else:
        return render_template('index.html', title = title, sources_news = sources)


@main.route('/results/<input_name>')
def search_results(input_name):
    '''
    View function to display the search results
    '''
    query_name_list = input_name.split(" ")
    query_name_format = "+".join(query_name_list)
    searched_movies = get_query(query_name_format)
    title = f'search results for {input_name}'
    return render_template('results.html', title = title, found_results = searched_movies)    

@main.route('/category')
def search():
    '''
    Find the article category and redirect
    '''
    general = get_query('general')

    return render_template('search-news.html', general = general)

@main.route('/entertainment')
def entertainment():
    '''
    See all entertainment related news
    '''
    entertainment = search_category('entertainment')

    return render_template('category.html', cat_results = entertainment)


@main.route('/sports')
def sports():
    '''
    See all sports related news
    '''
    sports = search_category('sports')

    return render_template('category.html',cat_results = sports)


@main.route('/health')
def health():
    '''
    See all sports related news
    '''
    health = search_category('health')

    return render_template('category.html', cat_results = health)

@main.route('/business')
def business():
    '''
    See all sports related news
    '''
    business = search_category('business')

    return render_template('category.html', cat_results = business)

@main.route('/technology')
def tech():
    '''
    See all technology related news
    '''
    technology = search_category('technology')

    return render_template('category.html', cat_results = technology)


@main.route('/BBC-NEWS')
def bbc():
    '''
    Get all bbc related news
    '''
    bbc = get_channel('bbc-news')

    return render_template('search-news.html', news_source = bbc)

@main.route('/BR-NEWS')
def cnn():
    '''
    Get all cnn related news
    '''
    Bleacher = get_channel('bleacher-report')

    return render_template('search-news.html', news_source = Bleacher)

@main.route('/ABC-NEWS')
def abc():
    '''
    Get all bbc related news
    '''
    abc = get_channel('abc-news')

    return render_template('search-news.html', news_source = abc)

@main.route('/FOX-NEWS')
def fox():
    '''
    Get all bbc related news
    '''
    fox = get_channel('fox-news')

    return render_template('search-news.html', news_source = fox)
