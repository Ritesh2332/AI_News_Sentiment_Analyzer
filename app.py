import streamlit as st
from scraper import NewsScraper

st.title("📰 AI News Sentiment Analyzer")

# 🎯 Category selection
category = st.selectbox(
    "Select Category",
    ["Top News", "Technology", "Business", "Sports", "Health", "Science"]
)

# 🧠 Map category to RSS URL
category_urls = {
    "Top News": "https://news.google.com/rss",
    "Technology": "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY",
    "Business": "https://news.google.com/rss/headlines/section/topic/BUSINESS",
    "Sports": "https://news.google.com/rss/headlines/section/topic/SPORTS",
    "Health": "https://news.google.com/rss/headlines/section/topic/HEALTH",
    "Science": "https://news.google.com/rss/headlines/section/topic/SCIENCE"
}

# Get selected URL
url = category_urls[category]

# Run scraper
scraper = NewsScraper(url)
xml_data = scraper.fetch()
data = scraper.parse(xml_data)

st.write(f"### Showing {category} News")

# Show more news (increase limit)
for news in data[:20]:
    st.subheader(news["title"])
    st.write(f"🧠 Sentiment: {news['sentiment']}")
    st.write(f"🔗 [Read more]({news['link']})")
    st.write("---")