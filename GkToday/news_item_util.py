import json
from model import NewsItem


def fill_date_wise_news(
    source_news_items: list[NewsItem],
    date_news_map: dict[str, list[NewsItem]] = {}
) -> dict[str, list[NewsItem]]:
    for news_item in source_news_items:
        date = news_item.date

        if date not in date_news_map.keys():
            date_news_map[date] = []

        date_news_map.get(date).append(news_item)

    return date_news_map


def remove_minority(
    date_news_map: dict[str, list[NewsItem]],
    required_size: int = 1
) -> dict[str, list[NewsItem]]:
    if required_size == 0 or len(date_news_map) <= required_size:
        return date_news_map

    news_freq_to_date = {}

    for date in date_news_map.keys():
        size = len(date_news_map[date])

        news_freq_to_date[size] = date

    if len(news_freq_to_date) == 1:
        # no minority found
        return date_news_map

    min_freq = min(news_freq_to_date.keys())
    date_for_min_freq = news_freq_to_date[min_freq]
    del date_news_map[date_for_min_freq]

    return remove_minority(
        date_news_map=date_news_map,
        required_size=required_size-1
    )


def news_items_to_json(
    news_items: list[NewsItem],
    indent: bool = False
) -> list[str]:
    '''
        This will convert the array of news items
        to the array of string as
    '''
    result_list = []

    for item in news_items:
        x = json.dumps(item.__dict__, indent=indent)
        result_list.append(x)

    return result_list
