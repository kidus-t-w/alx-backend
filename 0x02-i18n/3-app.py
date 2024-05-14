#!/usr/bin/env python3
"""A simple flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config class for Flask app

    This class defines the configuration for the Flask app. It includes
    the supported languages, the default locale, and the default timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select and return appropriate locale

    Returns:
        str: Locale code
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the index page.

    Returns:
        HTML: The rendered index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
