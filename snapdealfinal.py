from lxml import html
import requests


class Snapdeal:

	def __init__(self, starting_url):
		self.starting_url = starting_url
		
	def crawl(self):
		return self.product_data(self.starting_url)
		
	
	
	def product_data(self,link):
		start_page = requests.get(link)
		tree = html.fromstring(start_page.text)
		
		name = tree.xpath('//h1[@class="pdp-e-i-head"]/text()')[0]
		price = tree.xpath('//span[@class="payBlkBig"]/text()')[0]
		rating = tree.xpath('//span[@class="avrg-rating"]/text()')[0]


		return Product(name, price, rating)

			
		
class Product:

	def __init__(self, name, price, rating):
		self.name = name
		self.price = price
		self.rating = rating

	def __str__(self):
		return("Name: "+self.name.encode('UTF-8')+ "\r\nPrice: "+ self.price.encode('UTF-8')+ "\r\nRating: "+ self.rating.encode('UTF-8') + "\r\n" )

links = [	'https://www.snapdeal.com/product/samsung-galaxy-s5-charcoal-black/899231383#bcrumbSearch:samsung%20galaxy%20s5', 			'https://www.snapdeal.com/product/iphone-6s-16gb-gold/623846347834#bcrumbSearch:apple%20iphone%206s',
		'https://www.snapdeal.com/product/lenovo-k3-note-16gb-black/627705225055#bcrumbSearch:lenovo|bcrumbLabelId:12', 		'https://www.snapdeal.com/product/lg-15-ton-3-star/652022196882#bcrumbLabelId:230',
		'https://www.snapdeal.com/product/videocon-1-ton-5-star/646904754378#bcrumbLabelId:230',
		'https://www.snapdeal.com/product/ifb-15-ton-3-star/1352826129#bcrumbLabelId:230',
		'https://www.snapdeal.com/product/sony-kdl43w800d-109-cm-43/672053439838#bcrumbSearch:sony%20bravia%20ultra%20hd%20uhd',
		'https://www.snapdeal.com/product/lg-43lh576t-108-cm-43/658986046777#bcrumbLabelId:64',
		'https://www.snapdeal.com/product/samsung-40j5100-1016-cm-40/657947891594#bcrumbLabelId:64']

for link in links:
	crawler = Snapdeal(link)
	data = crawler.crawl()
	print data	

