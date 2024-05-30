# import website package
# grab create_app function
# use it & actually create an application & run it
# website is a python package, so when __init__.py is inside a folder
# it becomes a python package, which means when you input the name 
# of the folder, it will by default run all the stuff in the __init__.py
# which means we can import anything that's defined in __init__.py like the create_app
from website import create_app

app = create_app()

# only if we RUN NOT IMPORT this file main.py are we going to execute the app.run
# you only want to run the web server if you actually RUN this file directly
if __name__ == '__main__':
    app.run(debug=True) # run flask application, start a web server, any changes to python code, it will automatically rerun