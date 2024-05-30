# flask application
from flask import Flask

# define function
def create_app():
    # initialize app
    app = Flask(__name__) # __name__ represents name of the file
    # encrypt/secure session data related to website
    app.config['SECRET_KEY'] = 'noey'

    # import blueprints
    from .views import views
    from .auth import auth

    # register blueprints with flask application
    # url_prefix is saying: "all of the URLs stored inside the blueprints file
    # how do I access them?"
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app