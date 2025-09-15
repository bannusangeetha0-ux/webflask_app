"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app  # imports the app from __init__.py

if __name__ == '__main__':
    # Default host and port
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    # Enable debug mode for development
    app.run(host=HOST, port=PORT, debug=True)
