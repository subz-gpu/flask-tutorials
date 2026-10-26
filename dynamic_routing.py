from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/about")
def about():
    return "welcome to about page"

@app.route("/contacts")
def contact():
    return "welcome to contacts"

@app.route("/users")
def users():
    return "hello users"

@app.route("/users/<name>/<course>")
def dynamic_users(name,course):
    return f"{name} is learning {course}"

if __name__ == "__main__":
    app.run(debug = True)  