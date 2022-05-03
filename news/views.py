from flask import Flask, render_template
# from requests import get_news 

app=Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

  news = get_news()

if __name__ == '__main__':
  app.run(debug=True)