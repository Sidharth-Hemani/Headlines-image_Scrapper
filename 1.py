from urllib.request import urlopen as uopen
from urllib.request import urlretrieve as img_d
from bs4 import BeautifulSoup as soup
def collected_info(url,date):		
	date=date.replace('/','')
	print(date)	
	url = url + date+'hl.html'	
	download_html = uopen(url)
	page_html = download_html.read()
	page_soup = soup(page_html,'lxml')
	news_feed = page_soup.find_all('a',{'target':'_new'})	
	for x in news_feed:	
		print(x.text)
print('Enter the date for headlines in DD/MM/YY format')
date = str(input())	
collected_info('http://www.rediff.com/issues/',date)
