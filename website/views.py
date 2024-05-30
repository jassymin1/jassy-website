# store standard routes for website
# where users can actually go to/navigate (ex: home page, anything not related
# to authentication)
# NEED to register blueprints to __init__.py
from flask import Blueprint

# define this file as a blueprint for the flask application
# has a bunch of URLs defined

# define the name of the blueprint
views = Blueprint('views', __name__)


# to define a view in flask = @nameofblueprint
# inside the function/bracket put URL to get to this end-point/route
@views.route('/')
# define a function
def home(): # function will run whenever we go to our URL & type in '/' to go to main page of website (whatever is inside of home if gonna run)
    return "<h1>Test</h1>"