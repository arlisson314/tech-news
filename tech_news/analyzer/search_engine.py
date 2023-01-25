from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in search]


# Requisito 7
def search_by_date(date):
    try:
        date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        search = search_news({"timestamp": {"$eq": date}})
        return [(new["title"], new["url"]) for new in search]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    search = search_news({"tags": {"$regex": tag, "$options": "i"}})
    # print(search)
    return [(new["title"], new["url"]) for new in search]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
