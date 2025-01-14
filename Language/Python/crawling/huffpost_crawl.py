﻿import bs4
import urllib.request
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.+?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

base_url = 'https://www.huffpost.com'

sub_menues = {'section':['us_news','world_news'],'entertainment':['arts','media']}

sub_menu_urls = []
for key in sub_menues:
    for i in range(len(sub_menues[key])):
        url = base_url+'/'+key+'/'+sub_menues[key][i]
        sub_menu_urls.append(url)

target_urls = []
for sub_menu_url in sub_menu_urls:
    for i in range(1,100):
        url = sub_menu_url+'?page='+str(i)
        target_urls.append(url)


crawl_urls = []
for target_url in target_urls:
    try:
        hdr = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive' }
        req = urllib.request.Request(target_urls[0], headers=hdr)
        url = urllib.request.urlopen(req)
        bsObjs = bs4.BeautifulSoup(url,'html.parser')
        
        for bsObj in bsObjs.findAll('a',{'aria-hidden':'true'}):
            href = bsObj['href']
            crawl_urls.append(href)
    except:
        print(target_url)

crawl_texts = []
for crawl_url in crawl_urls:
    try:
        hdr = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive' }
        req = urllib.request.Request(crawl_url, headers=hdr)
        url = urllib.request.urlopen(req)
        bsObjs = bs4.BeautifulSoup(url,'html.parser')
        raw_html = str(bsObjs.findAll('div',{'class':'content-list-component yr-content-list-text text'})).replace('\n','') 
        context = cleanhtml(raw_html)
        crawl_texts.append(context)
    except:
        print(crawl_url)

with open('huffpost_crawl.txt', 'w') as f:
    for text in crawl_texts:
        f.write("%s\n" % text)    