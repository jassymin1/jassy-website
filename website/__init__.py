# flask application
from flask import Flask

# define function
def create_app():
    # initialize app
    app = Flask(__name__) # __name__ represents name of the file
    # encrypt/secure session data related to website
    app.config['SECRET_KEY'] = 'noey'

    return app