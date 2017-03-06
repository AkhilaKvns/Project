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

links = ['https://www.snapdeal.com/product/samsung-galaxy-s5-charcoal-black/899231383#bcrumbSearch:samsung%20galaxy%20s5', 'https://www.snapdeal.com/product/iphone-6s-16gb-gold/623846347834#bcrumbSearch:apple%20iphone%206s','https://www.snapdeal.com/product/moto-g-turbo-edition-16gb/681429229319']

for link in links:
	crawler = Snapdeal(link)
	data = crawler.crawl()
	print data	

