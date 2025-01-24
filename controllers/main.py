# Description: This file contains the main logic for fetching the latest and top news from the Indian Express website. It defines two functions, getLatestNews and getTopNews, to fetch the latest and top news, respectively. 
# The getLatestNews function fetches the latest news from the Indian Express website and saves the data in a CSV file named latest_news.csv in the data directory. 
# Similarly, the getTopNews function fetches the top news from the Indian Express website and saves the data in a CSV file named top_news.csv in the data directory. 
# Both the functions also return the fetched data as a list of dictionaries containing the title, URL, time, image URL, image alt text, and summary of each news article. In case of an error while fetching the data, an exception is raised.

# Importing required libraries
import requests
from bs4 import BeautifulSoup
import csv
import os

# Function to fetch the latest news from the Indian Express website
def getLatestNews(url: str = "https://indianexpress.com/latest-news/"):
    try:
        # Making a GET request to the URL and parsing the HTML content using BeautifulSoup
        req = requests.get(url)
        req.raise_for_status()
        html = req.text
        soup = BeautifulSoup(html, "html.parser").find_all(class_="articles")

        #  List to store the extracted data from each news article
        data = []
        # Looping through each news article and extracting the title, URL, time, image URL, image alt text, and summary
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
        
        # Writing the extracted data to a CSV file named latest_news.csv in the data directory
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
        # Handling exceptions and raising an error message in case of an error
        print(f"An error occurred while fetching data: {e}")
        raise e


# Function to fetch the top news from the Indian Express website 
def getTopNews(url: str = "https://indianexpress.com/top-news/"):
    try:
        # Making a GET request to the URL and parsing the HTML content using BeautifulSoup
        req = requests.get(url)
        req.raise_for_status()
        html = req.text
        soup = BeautifulSoup(html, "html.parser").find_all(class_="latest-articles")

        # List to store the extracted data from each news article
        data = []
        # Looping through each news article and extracting the title, URL, time, image URL, image alt text, and summary
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
        
        # Writing the extracted data to a CSV file named top_news.csv in the data directory
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
        # Handling exceptions and raising an error message in case of an error
        print(f"An error occurred while fetching data: {e}")
        raise e


# Main function to fetch the latest or top news based on user input if the script is run directly
if __name__ == "__main__":

    n = input("Enter 1 for Latest News and 2 for Top News: ")
    if n == "1":
        getLatestNews()
        print("Latest News Fetched and saved in data/latest_news.csv")
    elif n == "2":
        getTopNews()
        print("Top News Fetched and saved in data/top_news.csv")
    else:
        print("Invalid Input")
