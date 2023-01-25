from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    # top_five_list = []
    news = find_news()
    news.sort(key=itemgetter("comments_count", "title"), reverse=True)

    if len(news) <= 5:
        return [(new["title"], new["url"]) for new in news]

    top_five_list = [news[i] for i in range(5)]

    return [(new["title"], new["url"]) for new in top_five_list]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
