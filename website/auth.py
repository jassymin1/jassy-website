from flask import Blueprint

auth = Blueprint('auth', __name__)

# define route for login, logout & sign up
@auth.route('/login')
# define login funtion
def login():
    return "<p>Login</p>" # return a P tag

# define logout function
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

# define sign up function
@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"