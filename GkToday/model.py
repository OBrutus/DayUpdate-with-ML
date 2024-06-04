class NewsItem:
    def __init__(self, title, description, date, link=None):
        self.title = title
        self.description = description
        self.date = date
        self.link = link


class GkTodayNewsItem(NewsItem):
    pass
