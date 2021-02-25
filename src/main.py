from flask import Flask, url_for, request
from flask import render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/') #tells flask what url should call the function in the line below.
def hello_world():
    return 'Yo, Angelo!'

@app.route('/swooce')
def swooce():
    return 'swooce...'

# Demonstrates receiving string variables and using them.
@app.route('/user/<username>')
def show_user_profile(username):
    return "User: %s" % escape(username)

# Demonstrates receiving integer variables and using them.
@app.route('/post/<int:post_id>') # <converter output type:variable to convert>
def show_post(post_id):
    return "Post: %d" % post_id # no escape needed.

# Demonstrates receiving path variables and using them.
# paths are like strings but will accept slashes
@app.route('/path/<path:subpath>')
def show_path(subpath):
    return "Subpath: %s" % escape(subpath)

# Note:
# You can place a trailing slash after a URL. This acts sorta like a folder...?
# If you access it in your web browser without the trailing slash, flask will redirect you ro
# the trailing slash page.
# If you don't use a trailing slash, the url is similar to a path-name for the file.
# Accessing it using a trailing slash will cause a 404. This keeps urls unique.


# Using url_for(functionName) to build a url to a specific function.
# This does things like handle escaping special characters and cases where you application is not
# in the url root like /myapplication instead of the usual / will be handled for you as well.
with app.test_request_context(): # Tells flask to behave like it's handling a handling a request
    print(url_for("hello_world"))
    print(url_for("swooce"))
    print(url_for("show_user_profile", username="Cosmic")) # You need to pass in the args as well!
    print(url_for("show_post", post_id=1337))
    print(url_for("show_path", subpath="/test/sub/path"))

# Playing with HTTP methods.
# Routes only handle GETs by default but can do more.
def login_stuff():
    return "Welcome to The GRID"

def login_form():
    return "If you immediately know the candlelight is fire, _____."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_stuff()
    else: # GET
        return login_form()


# Instead of generating HTML in a python script, you can use the template engine, Jinja2, that
# comes with Flask. Give the template name and variables to pass to it.
# place from flask import render_template at the top of the file.
@app.route('/template_test')
@app.route('/template_test/<name>')
def template_test(name):
    return render_template('template_test.html', name=name)