# Description: This file contains the main code for the Flask app. It defines the routes and the functions to render the home, latest-news, and top-news pages. It also imports the `getTopNews` and `getLatestNews` functions from controllers/main.py to fetch the news data.
# The home route renders the home page using a Jinja2 template. The latest-news and top-news routes fetch the news data using the `getLatestNews` and `getTopNews` functions, respectively, and render the corresponding pages using Jinja2 templates. In case of an exception, an error message is returned.

# Importing required libraries
from flask import Flask
import requests
from jinja2 import Environment, FileSystemLoader
# Importing the getTopNews and getLatestNews functions from controllers/main.py to fetch the news data 
from controllers.main import getTopNews, getLatestNews

# Initializing the Flask app
app = Flask(__name__)


# Defining the home route
@app.route("/")
# Function to render the home page
def home():
    try:
        # Rendering the home page using Jinja2 template placed in the templates directory
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("index.html")
        return template.render()

    except requests.exceptions.RequestException as e:
        # Returning a message in case of an exception
        return {"message": "Failed to connect to the server"}


# Defining the latest-news route
@app.route("/latest-news")
# Function to render the latest news page
def latest():
    try:
        # Fetching the latest news using the getLatestNews function from controllers/main.py
        res = getLatestNews()
        # Rendering the latest news page using Jinja2 template placed in the templates directory
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("latest.html")
        return template.render(news=res)

    except requests.exceptions.RequestException as e:
        # Returning a message in case of an exception
        return {"message": "Failed to connect to the server"}


# Defining the top-news route
@app.route("/top-news")
# Function to render the top news page
def top():
    try:
        # Fetching the top news using the getTopNews function from controllers/main
        res = getTopNews()
        # Rendering the top news page using Jinja2 template placed in the templates directory
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("top.html")
        return template.render(news=res)

    except requests.exceptions.RequestException as e:
        # Returning a message in case of an exception
        return {"message": "Failed to connect to the server"}
