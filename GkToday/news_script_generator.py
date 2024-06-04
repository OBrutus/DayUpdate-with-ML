import sys

import web_util
import time
import repository_layer
import string_util

from gk_today import GkTodayUrl
from gk_today import GkTodayUtil

from bs4 import BeautifulSoup

if __name__ == '__main__':
    url_iterator = GkTodayUrl()

    raw_html, err = web_util.get_html_from_web(url_iterator.next())
    # html_str = str(raw_html, 'UTF-8')
    html_str = raw_html


    # repository_layer.raw_file_store(str(time.time_ns()), html_str)
    # if err:
    #     print('Error occured while fetching the URL, exiting')
    #     sys.exit(1)

    soup = BeautifulSoup(html_str, 'html.parser')

    result_set = soup.find_all(True, {
        'id': ['list']
    })

    gk_today_util = GkTodayUtil()
    news_title = []
    for result in result_set:

        heading_text = result.find('a').text
        heading_link = result.find('a')['href']

        heading_text = str.strip(heading_text)
        heading_text = string_util.remove_escape_sequence(heading_text)
        heading_text = string_util.remove_spaces(heading_text)

        description_summary = result.find_next('p').text
        description_summary = string_util.remove_escape_sequence(description_summary)
        description_summary = string_util.remove_spaces(description_summary)

        news_title.append(gk_today_util.get_news_headline(result))
