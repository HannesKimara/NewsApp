from flask import render_template
from . import main
from ..request import get_sources, process_sources

@main.route("/")
def index():
    news_sources = get_sources()

    data = process_sources(news_sources)
    
    return render_template('index.html', sources = data)
