from lxml import html
from bs4 import BeautifulSoup
import requests


class Paytm:

	def __init__(self, starting_url):
		self.starting_url = starting_url
		
	def crawl(self):
		return self.product_data(self.starting_url)
		
	
	
	def product_data(self,link):
		start_page = requests.get(link)
		soup = BeautifulSoup(start_page.text, 'html.parser')
		#tree = html.fromstring(start_page.text)
		name = soup.find(class_= "NZJI").text
		price = soup.find(class_= "_1d5g").text


		return Product(name, price)

			
		
class Product:

	def __init__(self, name, price):
		self.name = name
		self.price = price
		

	def __str__(self):
		return("Name: "+self.name.encode('UTF-8')+ "\r\nPrice: "+ self.price.encode('UTF-8')+ "\r\n" )

links= ['https://paytm.com/shop/p/samsung-galaxy-s5-black-MOBSAMSUNG-GALAPUSH59554B5751030?src=search-grid&tracker=autosuggest%7C66781%7Csamsung%20galaxy%20s5%2016%20gb%20black%7Cgrid%7CSearch%7C%7C20%7Cproduction&site_id=1&child_site_id=1','https://paytm.com/shop/p/apple-iphone-6s-16-gb-gold-MOBAPPLE-IPHONEDYNA1639482FD73195?src=search-grid&tracker=organic%7C66781%7Capple%20iphone%206s%7Cgrid%7CSearch%7C%7C13%7Cproduction&site_id=1&child_site_id=1','https://paytm.com/shop/p/moto-g-turbo-edition-black-MOBMOTO-G-TURBODIVI297133FF94FDDC?src=search-grid&tracker=organic%7C66781%7Cmoto%20g%20turbo%20edition%7Cgrid%7CSearch%7C%7C1%7Cproduction&site_id=1&child_site_id=1']

for link in links:
	crawler = Paytm(link)
	data= crawler.crawl()
	print data



