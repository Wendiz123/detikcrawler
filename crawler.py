import requests
from bs4 import BeautifulSoup
import urllib, os

def getCrawler(url):
    r = requests.get(url)

    if r.status_code == 200:
        print 'Parsing %s : ' % url
        soup = BeautifulSoup(r.text, "html.parser")
        print 'Jumlah Image : %s' % len(soup.find_all('img'))

        for imgnya in soup.find_all('img'):
            src = imgnya.get('src')
            if src.startswith('//'):
                file_img = 'http:%s' % src
            elif src.startswith('http://') or src.startswith('https://'):
                file_img = src
            else:
                file_img = url +'/'+ src

            #print file_img
            file_size_img = urllib.urlopen(file_img).info()['Content-Length']
            print 'Size image %s = %s bytes' % (imgnya.get('src'), file_size_img)
    else:
        print 'Can\'t Access Website. Status : %s' % r.status_code

getCrawler("http://detik.com")
print 'Done'