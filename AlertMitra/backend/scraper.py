import requests
from bs4 import BeautifulSoup

def get_disaster_updates():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("a", class_="gs-c-promo-heading")
    
    for article in articles:
        title = article.text.strip()
        link = "https://www.bbc.com" + article["href"]
        return {"title": title, "details": link}
    
    return {"title": "No updates", "details": "No recent disasters found."}