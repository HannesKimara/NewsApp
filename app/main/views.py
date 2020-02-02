from flask import render_template, redirect, url_for
from . import main
from ..request import get_sources, process_sources

@main.route("/")
def index():
    news_sources = get_sources()

    data = process_sources(news_sources)
    
    return render_template('index.html', sources = data)

@main.route("/articles/")
def red_articles():
    return redirect(url_for('main.index'))

@main.route("/articles/<source_id>")
def articles(source_id = None):
    return render_template("articles.html", source_id = source_id)