from flask import Flask
from news import views
from config import config_options


def create_app(config_name):
  app = Flask(__name__)



if __name__ == '__main__':
  app.run(debug=True)