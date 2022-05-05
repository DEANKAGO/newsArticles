from config import config_options
from flask import Flask
import os


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    return app


if __name__ == "__main__":
    app = create_app(os.environ.get('FLASK_ENV'))
    app.run()
