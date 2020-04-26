import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import master
import os
#import requests

def init():
	print('Hii '+os.getlogin() +' opening .... ')
	if sys.argv.__len__() > 1 :
		firstOption=sys.argv[1]
		if firstOption=='-c' or firstOption=='-C':
			print('You sre in customized mode ...')
			print('This Customisation last only uptill current session.')
			master.config.verboseCustomize()
		else:
			print('Invalid parameter specified')


#do not prompt for next jst do next



def main():
	news_url="http://news.google.com/news/rss"
	client=urlopen(news_url)
	page=client.read()
	client.close()

	soup_page=BeautifulSoup(page, "xml")
	news_list=soup_page.findAll("item")

	for news in news_list:
		text=news.title.text
		text+='\n'
		f=open('news.txt','w')
		f.write(text)
		master.printNews(news)
		if(master.config.autoPlay <= 0):
			ch=input("Continue / GetMoreInfo / Exit [default: Continue] \n[c, i, e] : ")
			if  ch=='e':
				break
			elif ch=='i':
				master.getMoreInfo(news)


if __name__=='__main__':
	init()
	main()
	print('\n\n'+'*'*5+'Done'+'*'*5)
