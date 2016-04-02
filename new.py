import urllib2
import urllib
from bs4 import BeautifulSoup as BS
import unicodedata

def india(url):
    src = urllib2.urlopen(url).read()
    bs = BS(src,"lxml")
    cnt = 0
    for i in bs.find_all("div", {"class": "search_pg_bg"}):
        for j in i.find_all("h2"):
            tmp = j.text
            cnt += 1
            if cnt < 11:
                new.write(str(cnt)+" .   ")
                temp = unicodedata.normalize('NFKD', tmp).encode('ascii','ignore')
                new.write(str(temp))

def jp(url):
    src = urllib2.urlopen(url).read()
    bs = BS(src,"lxml")
    cnt = 0
    for n in bs.find_all("div", {"class": "main_content"}):
        for i in n.find_all("h1"):
            tmp = i.string
            cnt += 1
            if cnt < 11:
                new.write(str(cnt)+" .   ")
                new.write(str(tmp)+"\n")

def aus(url):
    src = urllib2.urlopen(url).read()
    bs = BS(src,"lxml")
    cnt = 0
    for n in bs.find_all("div", {"class": "story-block "}):
        for i in n.find_all("a"):
            tmp = i.string
            cnt += 1
            if cnt < 11:
                new.write(str(cnt)+" .   ")
                new.write(str(tmp)+"\n")

def usa(url):
    src = urllib2.urlopen(url).read()
    bs = BS(src,"lxml")
    cnt = 0
    for n in bs.find_all("div", {"class": "listing-standard-lead "}):
        for i in n.find_all("h3"):
            tmp = i.string
            temp = unicodedata.normalize('NFKD', tmp).encode('ascii','ignore')
            cnt += 1
            if cnt < 11:
                new.write(str(cnt)+" .   ")
                new.write(str(temp)+"\n")

def uk(url):
    src = urllib2.urlopen(url).read()
    bs = BS(src,"lxml")
    cnt = 0
    for n in bs.find_all("span", {"class": "headline headline--normal headline--section-top-stories"}):
            tmp = n.string
            temp = unicodedata.normalize('NFKD', tmp).encode('ascii','ignore')
            cnt += 1
            if cnt < 11:
                new.write(str(cnt)+" .   ")
                new.write(str(temp)+"\n")


if __name__  == '__main__':
    new = open('new.txt','w')
    url = "http://www.hindustantimes.com/top-news"
    new.write("India : "+"\n")
    india(url)
    url = "http://www.japantimes.co.jp/news/national/"
    new.write("\n" + "Japan : "+"\n")
    jp(url)
    url = "http://www.news.com.au/national/breaking-news"
    new.write("\n" + "Australia : " + "\n")
    aus(url)
    url = "http://www.cbsnews.com/us/"
    new.write("\n" + "USA : " + "\n")
    usa(url)
    url = "http://news.sky.com/uk"
    new.write("\n" + "UK : " + "\n")
    uk(url)