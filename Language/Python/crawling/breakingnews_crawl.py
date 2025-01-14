﻿import bs4
import urllib.request
import re

urls = ['https://breakingnewsenglish.com/easy-news-english.html',
      'https://breakingnewsenglish.com/simple-english-news.html',
      'https://breakingnewsenglish.com/easy-english-news.html',
      'https://breakingnewsenglish.com/graded-news-stories.html',
      'https://breakingnewsenglish.com/graded-news-articles.html',
      'https://breakingnewsenglish.com/english-news-readings.html',
      'https://breakingnewsenglish.com/news-for-kids.html']

def cleanhtml(raw_html):
    cleanr = re.compile('<.+?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

crawl_urls = []
root_url = 'https://breakingnewsenglish.com/'
for url in urls:
    ur = urllib.request.urlopen(url)
    bsObj = bs4.BeautifulSoup(ur,"html.parser")
    context = bsObj.find('ul',{"class":"list-class"})
    lis = context.findAll("li")
    for li in lis:
        href = root_url+li.find('a')['href']
        crawl_urls.append(href)

crawl_text = []
for crawl_url in crawl_urls:
    try:
        crawl = urllib.request.urlopen(crawl_url)
        bsObj = bs4.BeautifulSoup(crawl,"html.parser")
        raw_html = str(bsObj.find('article')).replace("\n","").replace('(adsbygoogle = window.adsbygoogle || []).push({});','')
        text = cleanhtml(raw_html)
        crawl_text.append(text)
        print(crawl_url+'succ')
    except:
        print(crawl_url+'fail')

with open('breakingnews.txt', 'w') as f:
    for text in crawl_text:
        f.write("%s\n" % text) 