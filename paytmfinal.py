from lxml import html
from bs4 import BeautifulSoup
import requests
from product_def import Product

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
		description = soup.find(class_="_1jlE").text


		return Product("paytm",self.starting_url,name, price,description)

			
		
# class Product:

# 	def __init__(self, name, price):
# 		self.name = name
# 		self.price = price
		

# 	def __str__(self):
# 		return("Name: "+self.name.encode('UTF-8')+ "\r\nPrice: "+ self.price.encode('UTF-8')+ "\r\n" )

# links= [	'https://paytm.com/shop/p/samsung-galaxy-s5-black-MOBSAMSUNG-GALAPUSH59554B5751030?src=search-grid&tracker=autosuggest%7C66781%7Csamsung%20galaxy%20s5%2016%20gb%20black%7Cgrid%7CSearch%7C%7C20%7Cproduction&site_id=1&child_site_id=1',
# 		'https://paytm.com/shop/p/apple-iphone-6s-16-gb-gold-MOBAPPLE-IPHONEDYNA1639482FD73195?src=search-grid&tracker=organic%7C66781%7Capple%20iphone%206s%7Cgrid%7CSearch%7C%7C13%7Cproduction&site_id=1&child_site_id=1',
# 		'https://paytm.com/shop/p/lenovo-k3-note-black-MOBLENOVO-K3-NOMOBI90229CC35855E?src=search-grid&tracker=autosuggest%7C66781%7Clenovo%20mobile%20phones%7Cgrid%7CSearch%7C%7C1%7Cproduction&site_id=1&child_site_id=1',
# 		'https://paytm.com/shop/p/lg-js-q18npxa-1-5-ton-3-star-split-ac-LARLG-JS-Q18NPXAPPL5825442D42D46?src=grid&tracker=%7C%7C%7C%7C%2Fg%2Felectronics%2Flarge-appliances%2Fair-conditioners/reco-v2%7C24838%7C1%7C%7C00000001C5440A8A6BC8E0297C11F2B8E72C1916%7C', 
# 		'https://paytm.com/shop/p/videocon-vsn33wv2-3-star-1-ton-split-ac-LARVIDEOCON-VSNBANG26861773BC6CDD?src=grid&tracker=%7C%7C%7C%7C%2Fg%2Felectronics%2Flarge-appliances%2Fair-conditioners/reco-v2%7C24838%7C1%7C%7C00000001C5440A8A6BC8E0297C11F2B8E72C1916%7C', 
# 		'https://paytm.com/shop/p/ifb-iacs18ka3tc-1-5-ton-3-star-split-ac-LARIFB-IACS18KASALE258075EC7BE2C5?src=grid&tracker=%7C%7C%7C%7C%2Fg%2Felectronics%2Flarge-appliances%2Fair-conditioners/reco-v2%7C24838%7C2%7C%7C00000001C5440A8A6BC8E0297C11F2B8E72C1916%7C',
# 		'https://paytm.com/shop/p/sony-kdl-43w800d-108cm-43-led-tv-full-hd-LARSONY-KDL-43WBEST182943E8D29DD4?src=grid&tracker=||||%2Fg%2Felectronics%2Faudio-video%2Ftelevisions/reco-v2|24843|1||000000014E57C0E78358939E8F41C4059135CE98|',
# 		'https://paytm.com/shop/p/lg-43lh576t-108-cm-43-led-tv-full-hd-LARLG-43LH576T-BANG2686178B3F0E0D?src=grid&tracker=||||%2Fg%2Felectronics%2Faudio-video%2Ftelevisions/reco-v2|24843|2||000000014E57C0E78358939E8F41C4059135CE98|',
# 		'https://paytm.com/shop/p/sony-kdl-43w950d-108cm-43-led-tv-full-hd-LARSONY-KDL-43WSONY2330508D4F73C4?src=grid&tracker=||||%2Fg%2Felectronics%2Faudio-video%2Ftelevisions/reco-v2|24843|13||000000014E57C0E78358939E8F41C4059135CE98|']

# for link in links:
# 	crawler = Paytm(link)
# 	data= crawler.crawl()
# 	print data





