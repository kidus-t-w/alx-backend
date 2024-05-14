#!/usr/bin/env python3
"""
A simple flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config class for Flask app

    This class defines the configuration for the Flask app. It includes
    the supported languages, the default locale, and the default timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """
    Renders the index page.

    Returns:
        HTML: The rendered index page.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
