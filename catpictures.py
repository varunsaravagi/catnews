from bs4 import BeautifulSoup
import urllib
from urllib2 import urlopen

url = 'http://www.funnycatpix.com/_pics/Eat_A_Snickers.htm'

img_count = 201
def make_soup(url):
	html = urlopen(url).read()	
	return BeautifulSoup(html)


def download_images(url,img_count):
	if img_count > 300:
		print url
		return
	soup = make_soup(url)
	imgViewer = soup.find(id="viewer")
	img_url = imgViewer.img['src']
	filename = 'images/'+str(img_count)+'.'+img_url.split('/')[-1].split('.')[-1]	
	print filename
	urllib.urlretrieve(img_url,filename)
	next_url = soup.find(id="photonav").div.a['href']
	download_images(next_url,img_count+1)

download_images(url,img_count)
