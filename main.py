"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'hey, what\'s that over there?!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'This is not the page you are looking for', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'KaBOOM: {}'.format(e), 500
