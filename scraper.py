import requests
from textblob import TextBlob
from bs4 import BeautifulSoup
from utils import save_to_csv
from utils import get_real_url
import pandas as pd

class NewsScraper:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        return response.content  # XML content

    def parse(self, xml_data):
        soup = BeautifulSoup(xml_data, "xml")
        articles = soup.find_all("item")

        data = []

        for article in articles:
            title = article.title.text
            raw_link = article.link.text
            link = get_real_url(article.link.text)
            pub_date = article.pubDate.text

             # ML part
            sentiment_score = TextBlob(title).sentiment.polarity

            if sentiment_score > 0:
                sentiment = "Positive"
            elif sentiment_score < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            data.append({
                "title": title,
                "link": link,
                "published": pub_date,
                "sentiment": sentiment
            })

        return data


    def run(self):
        xml_data = self.fetch()
        data = self.parse(xml_data)
        save_to_csv(data)

if __name__ == "__main__":
    scraper = NewsScraper("https://news.google.com/rss")
    scraper.run()