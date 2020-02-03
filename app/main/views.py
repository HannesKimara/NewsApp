from flask import render_template, redirect, url_for
from . import main
from ..request import get_sources, process_sources, get_articles, process_articles

@main.route("/")
def index():
    news_sources = get_sources()
    data = process_sources(news_sources)
    
    return render_template('index.html', sources = data)

@main.route("/articles/")
def red_articles():
    return redirect(url_for('main.index'))

@main.route("/articles/<source_id>")
def articles(source_id):
    source_articles = get_articles("everything", {"sources": str(source_id)})
    if source_articles == False:
        return redirect(url_for('main.index'))

    data = process_articles(source_articles)

    return render_template("articles.html", headlines = data)

@main.route("/category/<category_name>")
def category(category_name):
    category_articles = get_articles("top-headlines",{"category": str(category_name), "country": "us"})
    if category_articles == False:
        return redirect(url_for('main.index'))

    data = process_articles(category_articles)

    return render_template("articles.html", headlines = data)