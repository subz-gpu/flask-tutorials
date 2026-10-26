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

if __name__ == "__main__":
    app.run(debug = True)  