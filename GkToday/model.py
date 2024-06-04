import time


class NewsItem:
    def __init__(
        self,
        title: str,
        date: str,
        description: str,
        link: str = None,
        source: str = None,
    ):
        self.title = title
        self.date = date
        self.description = description
        self.link = link

        current_time = time.time()
        self.created_at = current_time
        self.updated_at = current_time

        self.source = source
        self.status = 'active'


class GkTodayNewsItem(NewsItem):
    pass


class GkTodayNewsHeadlineItem(NewsItem):
    def __init__(
        self,
        title: str,
        date: str,
        description_summary: str,
        link: str
    ):
        super().__init__(
            title=title,
            date=date,
            description=description_summary,
            link=link,
            source="gktoday.in"
        )
        self.is_headline = True
