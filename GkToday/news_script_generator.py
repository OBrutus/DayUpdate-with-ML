import sys

import web_util
import time
import repository_layer
import string_util
import news_item_util

from gk_today import GkTodayUrl
from gk_today import GkTodayUtil
from model import GkTodayNewsHeadlineItem

from bs4 import BeautifulSoup

NEWS_PER_DAY_LIMIT = 1


def create_news_headline_items(
    html_str: str
) -> list[GkTodayNewsHeadlineItem]:
    soup = BeautifulSoup(html_str, 'html.parser')

    result_set = soup.find_all(True, {
        'id': ['list']
    })

    news_headlines = []
    for result in result_set:

        heading_text = result.find('a').text
        heading_link = result.find('a')['href']

        heading_text = str.strip(heading_text)
        heading_text = string_util.remove_escape_sequence(heading_text)
        heading_text = string_util.remove_spaces(heading_text)

        date_of_publishing = result.find_next('div').find('span').text
        date_of_publishing = str.strip(date_of_publishing)

        description_summary = result.find_next('p').text
        description_summary = str.strip(description_summary)
        description_summary = string_util.remove_escape_sequence(description_summary)
        description_summary = string_util.remove_spaces(description_summary)

        headline_item = GkTodayNewsHeadlineItem(
            heading_text,
            date=date_of_publishing,
            description_summary=description_summary,
            link=heading_link
        )

        news_headlines.append(headline_item)

    return news_headlines


def main():
    url_iterator = GkTodayUrl()

    raw_html, err = web_util.get_html_from_web(url_iterator.next())
    # html_str = str(raw_html, 'UTF-8')
    html_str = raw_html

    # repository_layer.raw_file_store(str(time.time_ns()), html_str)
    # if err:
    #     print('Error occured while fetching the URL, exiting')
    #     sys.exit(1)

    date_news_map = {}
    while True:
        news_items = create_news_headline_items(html_str=html_str)
        date_news_map = news_item_util.fill_date_wise_news(
            news_items,
            date_news_map
        )

        if len(date_news_map) > NEWS_PER_DAY_LIMIT:
            # remove the less majority entry
            # break the flow
            date_news_map = news_item_util.remove_minority(
                date_news_map,
                NEWS_PER_DAY_LIMIT
            )
            break

        # TODO: remove this once done with mock praciticing
        break

    # at this point we have date_news_map fill with all the headlines
    list_of_news_items = list(date_news_map.values())[0]
    formatted_json_array = news_item_util.news_items_to_json(
        list_of_news_items,
        indent=True
    )

    sanitized_news_items_str = str(formatted_json_array)
    sanitized_news_items_str = str.strip(sanitized_news_items_str)
    sanitized_news_items_str = string_util.remove_escape_sequence(
        sanitized_news_items_str
    )
    # TODO: if trying to save the result to a file
    # it contains lot's of start single quote which might have
    # been added as a part of conversion from object to json, remove it
    repository_layer.raw_file_store(
        title=str(time.time()) + '.news.json',
        data=sanitized_news_items_str
    )


if __name__ == '__main__':
    main()
