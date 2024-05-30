# store standard routes for website
# where users can actually go to/navigate (ex: home page, anything not related
# to authentication)
from flask import Blueprint

# define this file as a blueprint for the flask application
# has a bunch of URLs defined

# define the name of the blueprint
views = Blueprint('views', __name__)