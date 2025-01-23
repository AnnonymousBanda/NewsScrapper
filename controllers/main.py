import requests
from bs4 import BeautifulSoup


def getLatest(url: str = "https://indianexpress.com/latest-news/"):
    try:
        req = requests.get(url)
        req.raise_for_status()
        html = req.text
        soup = BeautifulSoup(html, "html.parser").find_all(class_="articles")
        print(f"Number of articles found: {len(soup)}")

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
                    "summary": summary.get_text(strip=True) if summary else "No Summary",
                }
            )
            
        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return []


getLatest()
