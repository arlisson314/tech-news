from tech_news.database import find_news
from operator import itemgetter
from collections import Counter


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
    news = find_news()
    all_categories = [new["category"] for new in news]
    top_five_list = sorted(
        Counter(all_categories).most_common(5), key=lambda x: (-x[1], x[0])
    )
    return [category[0] for category in top_five_list]
