from lxml import html
from bs4 import BeautifulSoup
import requests
from product_def import Product
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
		description = tree.xpath('//div[@class="itemAttr"]/text()')[0]

		#print "Name: " + name
		#print "Price: " + price

		# soup = BeautifulSoup(start_page.text, 'html.parser')
		# name = soup.find('h1', id_="itemTitle").text
		# price = soup.find('span', id_="prcIsum").text
		# rating = soup.find('span', class_="avrg-rating").text
		# description = ""
		# for desc in soup.find_all('div', class_="itemAttr"):
		# 	description += desc.text 
		
		
		return Product("ebay",self.starting_url,name,price, description)

			
		
# class Product:

# 	def __init__(self, name, price):
# 		self.name = name
# 		self.price = price
		
# 	def __str__(self):
# 		return("Name: "+self.name.encode('UTF-8')+ "\r\nPrice: "+ self.price.encode('UTF-8')+ "\r\n")

# links = [
# 		'http://www.ebay.in/itm/Samsung-Galaxy-S5-G900H-16GB-BLACK-SEALED-PACK-PIECE-/292039926996?hash=item43feefa4d4:g:78UAAOSw~AVYqWuu',
# 		'http://www.ebay.in/itm/Apple-iPhone-6S-Latest-Model-16GB-Gold-Smartphone-/222427104429?hash=item33c9b044ad:g:fRIAAOSwax5YsCzi',
# 		'http://www.ebay.in/itm/Lenovo-K3-Note-BLACK-PROMO-/222423562697?hash=item33c97a39c9:g:eUAAAOSwCU1YpE4I',
# 		'http://www.ebay.in/itm/LG-SMART-Inverter-Split-AC-1-5Ton-Air-Conditioner-Brand-New-Sealed-VAT-Bill-/152427954534?hash=item237d6a0166:g:OaEAAOSwcUBYIGvC',
# 		 'http://www.ebay.in/itm/Videocon-VSN33-WV2-MDA-SDA-SDM-Split-AC-1-Ton-3-Star-Rating-White-Aluminium-/262872296435?hash=item3d3468ebf3:g:M~kAAOSwXYtYs-ed',
# 		 'http://www.ebay.in/itm/IFB-Air-Conditioner-IACS18KA3TGC-1-5-Ton-3-Star-/142286644552?hash=item2120f1e548:g:D~oAAOSw32lYq9qj',
# 'http://www.ebay.com/itm/Sony-KDL48R510C-48-48-Inch-Full-HD-1080p-Smart-LED-TV-2015-Model-Built-in-WiFi-/272501553775?hash=item3f725bba6f:g:Y3oAAOSwNRdX5T30',
# 		'http://www.ebay.com/itm/LG-43UH6107-43-quot-108-cm-quot-Smart-TV-webOS-3-0-4K-/172444939241?hash=item282684f3e9:g:lOkAAOSwnHZYUTpJ',
# 		'http://www.ebay.com/itm/TV-SAMSUNG-SMARTV-102cm-3D-Tres-peu-utilise-Offre-a-part-pour-la-XBOX-/222429193933?hash=item33c9d026cd:g:iOEAAOSw4A5YrbOg']

# for link in links:
# 	crawler = Ebay(link)
# 	data = crawler.crawl()
# 	print data


