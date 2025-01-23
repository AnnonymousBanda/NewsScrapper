from flask import Flask
import requests

from controllers.main import getTopNews, getLatestNews

app = Flask(__name__)


@app.route("/")
def home():
    try:
        return {"message": "Welcome to the Indian Express API"}

    except requests.exceptions.RequestException as e:
        return "<p>Failed to connect to the server</p>"


@app.route("/latest-news")
def latest():
    try:
        res = getLatestNews()
        return res

    except requests.exceptions.RequestException as e:
        return "<p>Failed to connect to the server</p>"


@app.route("/top-news")
def top():
    try:
        res = getTopNews()
        return res

    except requests.exceptions.RequestException as e:
        return "<p>Failed to connect to the server</p>"
