import bs4

from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as ureq
myurl = 'http://www.espncricinfo.com/series/8768/scorecard/1124818/Australia-vs-Bangladesh-10th-match,-Group-B-hong-kong-world-sixes/'

uclient = ureq(myurl)

pagehtml = uclient.read()

uclient.close()

pagesoup = soup(pagehtml, "html.parser")

#pagesoup.h1

#pagesoup.body.span

containers = pagesoup.findAll("div",{"class":"flex-row"})

#containers[0]

#containers[0].text

#n = len(containers)
#for i in range(n):
#print(containers[i].text)

runs = pagesoup.findAll("div",{"class":"cell runs"})
bat = pagesoup.findAll("div",{"class":"cell batsmen"})
p = len(bat)
for i in range(p):
    print(bat[i].text,runs[i*5].text,runs[5*i+1].text,runs[5*i+2].text,runs[5*i+3].text,runs[5*i+4].text)

bowl = pagesoup.findAll("tr")
q= len(bowl)
for i in range(q):
    print(bowl[i].text)
