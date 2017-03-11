from bs4 import BeautifulSoup
import requests
from product_def import Product

class Snapdeal:

	def __init__(self, starting_url):
		self.starting_url = starting_url
		
	def crawl(self):
		return self.product_data(self.starting_url)
		
	
	
	def product_data(self,link):
		start_page = requests.get(link)
		# tree = html.fromstring(start_page.text)
		soup = BeautifulSoup(start_page.text, 'html.parser')
		name = soup.find('h1', class_="pdp-e-i-head").text
		price = soup.find('span', class_="payBlkBig").text
		rating = soup.find('span', class_="avrg-rating").text
		description = ""
		for desc in soup.find_all('div', class_="detailssubbox"):
			description += desc.text 
		

		return Product("snapdeal",self.starting_url, name, price, rating,description)

			
		
# links = [	'https://www.snapdeal.com/product/samsung-galaxy-s5-charcoal-black/899231383#bcrumbSearch:samsung%20galaxy%20s5', 			'https://www.snapdeal.com/product/iphone-6s-16gb-gold/623846347834#bcrumbSearch:apple%20iphone%206s',
# 		'https://www.snapdeal.com/product/lenovo-k3-note-16gb-black/627705225055#bcrumbSearch:lenovo|bcrumbLabelId:12', 		'https://www.snapdeal.com/product/lg-15-ton-3-star/652022196882#bcrumbLabelId:230',
# 		'https://www.snapdeal.com/product/videocon-1-ton-5-star/646904754378#bcrumbLabelId:230',
# 		'https://www.snapdeal.com/product/ifb-15-ton-3-star/1352826129#bcrumbLabelId:230',
# 		'https://www.snapdeal.com/product/sony-kdl43w800d-109-cm-43/672053439838#bcrumbSearch:sony%20bravia%20ultra%20hd%20uhd',
# 		'https://www.snapdeal.com/product/lg-43lh576t-108-cm-43/658986046777#bcrumbLabelId:64',
# 		'https://www.snapdeal.com/product/samsung-40j5100-1016-cm-40/657947891594#bcrumbLabelId:64']


# for link in links:
# 	crawler = Snapdeal(link)
# 	data = crawler.crawl()
# 	print data	

