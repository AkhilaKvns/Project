from lxml import html
import requests


class Ebay:

	def __init__(self, starting_url):
		self.starting_url = starting_url

	def crawl(self):
		return self.product_data(self.starting_url)
		
	
	def product_data(self,link):
		start_page = requests.get(link)
		tree = html.fromstring(start_page.text)
		
		name = tree.xpath('//h1[@id="itemTitle"]/text()')[0]
		price = tree.xpath('//span[@id="prcIsum"]/text()')[0]

		#print "Name: " + name
		#print "Price: " + price
		
		return Product(name,price)

			
		
class Product:

	def __init__(self, name, price):
		self.name = name
		self.price = price
		
	def __str__(self):
		return("Name: "+self.name.encode('UTF-8')+ "\r\nPrice: "+ self.price.encode('UTF-8')+ "\r\n")

links = ['http://www.ebay.in/itm/Samsung-Galaxy-S5-G900H-16GB-BLACK-SEALED-PACK-PIECE-/292039926996?hash=item43feefa4d4:g:78UAAOSw~AVYqWuu','http://www.ebay.in/itm/Apple-iPhone-6S-Latest-Model-16GB-Gold-Smartphone-/222427104429?hash=item33c9b044ad:g:fRIAAOSwax5YsCzi','http://www.ebay.in/itm/Moto-G-Turbo-Edition-Black-16GB-XT1557-/332032383500?hash=item4d4eac1a0c:g:2vcAAOSwh2xYAOKq']

for link in links:
	crawler = Ebay(link)
	data = crawler.crawl()
	print data

