﻿import bs4
import urllib.request
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.+?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

target_urls = []
for i in range(1,241):
    target_urls.append('http://www.chinadaily.com.cn/china/governmentandpolicy/page_'+str(i)+'.html')
    
crawl_urls = []
for target_url in target_urls:
    url = urllib.request.urlopen(target_url)
    bsObjs = bs4.BeautifulSoup(url,"html.parser")
    bsObjs = bsObjs.findAll('a')
    for bsObj in bsObjs:
        href = bsObj['href'].replace('//','')
        if ('/a/' in href):
            crawl_urls.append(href)
            

crawl_text = []
for crawl_url in crawl_urls:
    try:
        hdr = { 'User-Agent' : 'foobar' }
        req = urllib.request.Request('http://'+crawl_url, headers=hdr)
        crawl = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(crawl,"html.parser")
        raw_html = str(bsObj.find('div',{'id':'Content'})).replace("\n","")
        text = cleanhtml(raw_html)
        crawl_text.append(text)
        
    except:
        
with open('china_crawl.txt', 'w') as f:
    for text in crawl_text:
        f.write("%s\n" % text) 