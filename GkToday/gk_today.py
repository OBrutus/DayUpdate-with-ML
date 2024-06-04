from model import GkTodayNewsItem
from bs4 import BeautifulSoup


class GkTodayUrl:
    def __init__(self):
        self.url = "https://www.gktoday.in/current-affairs/page/"
        self.counter = 1

    def next(self) -> str:
        resultant_url = self.get()
        self.counter += 1
        return resultant_url

    def get(self) -> str:
        return self.url + str(self.counter)


class GkTodayUtil:
    @staticmethod
    def get_news_headline(html_headline_str: str) -> GkTodayNewsItem:
        soup = BeautifulSoup(html_headline_str, 'lxml')
        soup.find('a')
