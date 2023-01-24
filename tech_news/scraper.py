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
    path = "a.next::attr(href)"
    next_page_link = Selector(text=html_content).css(path).get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    tech_news = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "comments_count": len(selector.css("div.comment-content").getall())
        or 0,
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "tags": selector.css("section.post-tags ul li a::text").getall(),
        "category": selector.css(".meta-category span.label::text").get(),
    }
    return tech_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
