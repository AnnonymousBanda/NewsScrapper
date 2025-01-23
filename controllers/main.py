import requests
from bs4 import BeautifulSoup
import csv
import os


def getLatestNews(url: str = "https://indianexpress.com/latest-news/"):
    try:
        req = requests.get(url)
        req.raise_for_status()
        html = req.text
        soup = BeautifulSoup(html, "html.parser").find_all(class_="articles")

        data = []
        for k in soup:
            title = k.find(class_="title")
            article_url = k.find("a")["href"]
            time = k.find(class_="date")
            image = k.find("img")
            summary = k.find("p")

            image_url = image["src"] if image else "No Image"
            image_alt = image["alt"] if image else "No Alt Text"

            data.append(
                {
                    "title": title.get_text(strip=True) if title else "No Title",
                    "url": article_url if article_url else "No URL",
                    "time": time.get_text(strip=True) if time else "No Time",
                    "image_url": image_url,
                    "image_alt": image_alt,
                    "summary": (
                        summary.get_text(strip=True) if summary else "No Summary"
                    ),
                }
            )

        with open(os.path.join("data", "latest_news.csv"), "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "title",
                    "url",
                    "time",
                    "image_url",
                    "image_alt",
                    "summary",
                ],
            )
            writer.writeheader()
            writer.writerows(data)

        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return []


def getTopNews(url: str = "https://indianexpress.com/top-news/"):
    try:
        req = requests.get(url)
        req.raise_for_status()
        html = req.text
        soup = BeautifulSoup(html, "html.parser").find_all(class_="latest-articles")

        data = []
        for k in soup:
            title = k.find(class_="latest-title")
            article_url = k.find("a")["href"]
            time = k.find(class_="latest-time")
            image = k.find("img")
            summary = k.find("p")

            image_url = image["src"] if image else "No Image"
            image_alt = image["alt"] if image else "No Alt Text"

            data.append(
                {
                    "title": title.get_text(strip=True) if title else "No Title",
                    "url": article_url if article_url else "No URL",
                    "time": time.get_text(strip=True) if time else "No Time",
                    "image_url": image_url,
                    "image_alt": image_alt,
                    "summary": (
                        summary.get_text(strip=True) if summary else "No Summary"
                    ),
                }
            )

        with open(os.path.join("data", "top_news.csv"), "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "title",
                    "url",
                    "time",
                    "image_url",
                    "image_alt",
                    "summary",
                ],
            )
            writer.writeheader()
            writer.writerows(data)

        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return {}

getLatestNews()