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
            file_size_img = urllib.urlopen(imgnya.get('src')).info()['Content-Length']
            print 'Size image %s = %s bytes' % (imgnya.get('src'), file_size_img)
    else:
        print 'Web can not Accessible. Status : %s' % r.status_code

getCrawler("http://detik.com")