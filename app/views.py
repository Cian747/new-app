from app.request import get_source
from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Nairobi Times'
    sources = get_source('entertainment')
    return render_template('index.html', title = title, sources_news = sources)