from app import create_app
from flask import render_template
import requests
import os

app = create_app(os.environ.get('FLASK_ENV'))

NEWS_API_KEY = os.environ.get('API_KEY')
NEWS_API_BASE_URL = "https://newsapi.org/v2/everything?q=Apple&from=2022-05-03&sortBy=popularity&apiKey=%s" % NEWS_API_KEY

# SOURCE_API_BASE_URL = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=%s" % NEWS_API_KEY

REUTERS_API_BASE_URL = "https://newsapi.org/v2/top-headlines?sources=reuters&apiKey=%s" % NEWS_API_KEY


@app.route('/')
def index():
    res = requests.get(NEWS_API_BASE_URL)
    list_of_articles = []
    if res.status_code == 200 and res.json()['status'].lower() == "ok":
        list_of_articles = res.json()['articles']
    # list_of_sources = []
    # for i in list_of_articles:
    #     list_of_sources.append(i['source']['name'])
    # sources_str = ', '.join(list_of_sources)
    return render_template('index.html', list_of_articles=list_of_articles)


@app.route('/bbc')
def bbc():
    res = requests.get(SOURCE_API_BASE_URL)
    list_of_articles = []
    if res.status_code == 200 and res.json()['status'].lower() == "ok":
        list_of_articles = res.json()['articles']
    return render_template('index.html', list_of_articles=list_of_articles, sources_str=['bbc'])


@app.route('/reuters')
def reuters():
    res = requests.get(REUTERS_API_BASE_URL)
    list_of_articles = []
    if res.status_code == 200 and res.json()['status'].lower() == "ok":
        list_of_articles = res.json()['articles']
    return render_template('index.html', list_of_articles=list_of_articles, sources_str=['reuters'])


if __name__ == '__main__':
    app.run()
