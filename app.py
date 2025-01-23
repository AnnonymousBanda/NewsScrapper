from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        r= requests.get("https://indianexpress.com")
        return "<h1>It works<h1>"+r.text

    except requests.exceptions.RequestException as e:
        return "<p>Failed to connect to the server</p>"
