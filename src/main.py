import flask

# Create a flask app
app = flask.Flask(__name__)

# Root route for app (example.com/)
@app.route("/")
def index():
    return "<h1>hello world!</h1><br><h3>use route /hi/<username> to recieve a greeting</h3>"

# Hi route without valid input
@app.route("/hi/")
def who():
    return "<h1>who are you?</h1>"

# Hi route with valid input
@app.route("/hi/<username>")
def greet(username):
    return f"<h1>hello, {username}!<h1>"

# Development server only, not for production
app.run()