from flask import Flask
import requests

from controllers.main import getTopNews, getLatestNews

app = Flask(__name__)


@app.route("/")
def home():
    try:
        return {"message": "Welcome to the News Scrapping API"}

    except requests.exceptions.RequestException as e:
        return {"message": "Failed to connect to the server"}


@app.route("/latest-news")
def latest():
    try:
        res = getLatestNews()
        return {
            "message": "Latest News Fetched and saved in data/latest_news.csv",
            "no_of_news": len(res),
            "date": res[0]["time"].split(" ")[1]+" "+res[0]["time"].split(" ")[2]+" "+res[0]["time"].split(" ")[3],
            "data": res,
        }

    except requests.exceptions.RequestException as e:
        return {"message": "Failed to connect to the server"}


@app.route("/top-news")
def top():
    try:
        res = getTopNews()
        return {
            "message": "Top News Fetched and saved in data/top_news.csv",
            "no_of_news": len(res),
            "date": res[0]["time"].split(" ")[1]+" "+res[0]["time"].split(" ")[2]+" "+res[0]["time"].split(" ")[3],
            "data": res,
        }

    except requests.exceptions.RequestException as e:
        return {"message": "Failed to connect to the server"}
