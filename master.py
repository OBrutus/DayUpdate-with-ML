import time
import analysis
from custom import Custom

config=Custom()

def getMoreInfo(news):
    eof=config.startOfLine+'\n'
    print('source: '+str(news.source.text), end=eof)
    print('link : '+str(news.source.link), end=eof)

def printNews(news):
    eof=config.startOfLine+'\n'

    print('autopla=',config.autoPlay)

    print(config.startOfLine+news.title.text, end=eof)
    print(news.pubDate.text, end=eof)

    if config.detailed:
        getMoreInfo(news)
    
    if config.immidiateAnalysis:
        analysis.analysisInfo(news.title.text)

    if config.autoPlay > 0:
        time.sleep(config.autoPlay)
    
    print(config.endOfNewsDelmiter)