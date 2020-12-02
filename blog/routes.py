from flask import render_template, url_for
from blog import app
from blog.models import Article
from pathlib import Path

@app.route('/')
@app.route('/home')
def home():
    articles=Article.query.all()
    return render_template('home.html', subheader="home", articles=articles)


@app.route('/about')
def about():
    return render_template('about.html', subheader="about")

@app.route('/article/<article>')
def post(article):
    return render_template(article)
