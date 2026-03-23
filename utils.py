import pandas as pd
import requests

def save_to_csv(data, filename="news.csv"):
    df = pd.DataFrame(data)
    df.drop_duplicates(inplace=True)
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

def get_real_url(google_url):
    try:
        response = requests.get(google_url, allow_redirects=True)
        return response.url
    except:
        return google_url