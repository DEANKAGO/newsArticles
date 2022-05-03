from app import create_app
from flask import render_template
import requests
import os

app = create_app(os.environ.get('FLASK_ENV'))

NEWS_API_KEY = os.environ.get('API_KEY')
NEWS_API_BASE_URL = "https://newsapi.org/v2/everything?q=Apple&from=2022-05-03&sortBy=popularity&apiKey=%s" % NEWS_API_KEY


@app.route('/')
def index():
    res = requests.get(NEWS_API_BASE_URL)
    list_of_articles = []
    if res.status_code == 200 and res.json()['status'].lower() == "ok":
        list_of_articles = res.json()['articles']
    return render_template('index.html', list_of_articles=list_of_articles)


if __name__ == '__main__':
    app.run()
