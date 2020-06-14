from bs4 import BeautifulSoup
from django.contrib.sites import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")


def extract_next_page(soup):
    """ Extract next page URL """
    next_page_news = parser.table.findAll('a', 'morelink')
        #next_page = next_page_news[0]['href']
    return next_page_news

print(extract_next_page(soup))