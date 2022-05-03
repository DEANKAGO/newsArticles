from flask import Flask
from news import views
from .config import DevConfig

app = Flask(__name__)

if __name__ == '__main__':
  app.run(debug=True)