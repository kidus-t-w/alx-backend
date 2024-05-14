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
    Get the locale for the request
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Executes before each request.

    Retrieves the user associated with the request and
    stores it in the global context.

    Returns:
        None
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
