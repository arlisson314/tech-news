import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    USER = {"user-agent": "Fake user-agent"}
    try:
        res = requests.get(url, headers=USER, timeout=3)
        sleep(1)
        res.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    return res.text


# Requisito 2
def scrape_updates(html_content):
    path = "div.cs-overlay a::attr(href)"
    get_links = Selector(text=html_content).css(path).getall()
    return get_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
