from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello world</h1>"

@app.route('/index')
def index():
    return "<h1>Index site</h1>"

app.run(host="0.0.0.0", port=8000)