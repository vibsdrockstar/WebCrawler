#spider webpage
import urlparse
import urllib
from vib20 import BeautifulSoup

url="http://rediff.com "

urls = [url] #stacks of urls to scrape
visited = [url] #historic records of urls

while len(urls)>0:
    try:
        htmltext=urllib.urlopen(urls[0]).read()
        except:
            print urls[0]
        soup = BeautifulSoup(htmltext)

        urls.pop(0)
        print len(urls)

        for tag in soup.findAll('a',href=True):
             tag['href']= urlparse.urljoin(url,tag['href'])
             if url in tag['href'] and tag['href'] not in visited:
                 urls.append(tag['href'])
                 visited.append(tag['href'])

print visited
            
