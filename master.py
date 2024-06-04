import time
import analysis
from custom import Custom

config = Custom()


def getMoreInfo(news):
    EOF = config.startOfLine+'\n'
    print('source: '+str(news.source.text), end=EOF)
    print('link : '+str(news.source.link), end=EOF)


def printNews(news):
    EOF = config.startOfLine+'\n'

    print('autopla=', config.autoPlay)

    print(config.startOfLine+news.title.text, end=EOF)
    print(news.pubDate.text, end=EOF)

    if config.detailed:
        getMoreInfo(news)

    if config.immidiateAnalysis:
        analysis.analysisInfo(news.title.text)

    if config.autoPlay > 0:
        time.sleep(config.autoPlay)

    print(config.endOfNewsDelmiter)
