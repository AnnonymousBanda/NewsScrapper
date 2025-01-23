from flask import Flask
import requests
from jinja2 import Environment, FileSystemLoader
from controllers.main import getTopNews, getLatestNews

app = Flask(__name__)


@app.route("/")
def home():
    try:
        env = Environment(loader = FileSystemLoader('templates'))
        template = env.get_template('index.html')
        return template.render()

    except requests.exceptions.RequestException as e:
        return {"message": "Failed to connect to the server"}


@app.route("/latest-news")
def latest():
    try:
        res = getLatestNews()
        env = Environment(loader = FileSystemLoader('templates'))
        template = env.get_template('latest.html')
        return template.render(news = res)

    except requests.exceptions.RequestException as e:
        return {"message": "Failed to connect to the server"}


@app.route("/top-news")
def top():
    try:
        res = getTopNews()
        env = Environment(loader = FileSystemLoader('templates'))
        template = env.get_template('top.html')
        return template.render(news = res)

    except requests.exceptions.RequestException as e:
        return {"message": "Failed to connect to the server"}
