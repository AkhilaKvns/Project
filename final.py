from ebayfinal import Ebay
from snapdealfinal import Snapdeal
from paytmfinal import Paytm


class Crawl:

	def __init__(self, starting_url, site):
		self.starting_url = starting_url
		self.site = site
		
	def crawl(self):
		if self.site == "ebay":
			self.logic = Ebay(self.starting_url)
		elif self.site == "snapdeal":
			self.logic = Snapdeal(self.starting_url)
		elif self.site == "paytm":
			self.logic = Paytm(self.starting_url)
		return self.logic.crawl()


links= [
		 ['https://paytm.com/shop/p/samsung-galaxy-s5-black-MOBSAMSUNG-GALAPUSH59554B5751030?src=search-grid&tracker=autosuggest%7C66781%7Csamsung%20galaxy%20s5%2016%20gb%20black%7Cgrid%7CSearch%7C%7C20%7Cproduction&site_id=1&child_site_id=1',"paytm"],
		# ['https://paytm.com/shop/p/apple-iphone-6s-16-gb-gold-MOBAPPLE-IPHONEDYNA1639482FD73195?src=search-grid&tracker=organic%7C66781%7Capple%20iphone%206s%7Cgrid%7CSearch%7C%7C13%7Cproduction&site_id=1&child_site_id=1',"paytm"],
		# ['https://paytm.com/shop/p/lenovo-k3-note-black-MOBLENOVO-K3-NOMOBI90229CC35855E?src=search-grid&tracker=autosuggest%7C66781%7Clenovo%20mobile%20phones%7Cgrid%7CSearch%7C%7C1%7Cproduction&site_id=1&child_site_id=1',"paytm"],
		# ['https://paytm.com/shop/p/lg-js-q18npxa-1-5-ton-3-star-split-ac-LARLG-JS-Q18NPXAPPL5825442D42D46?src=grid&tracker=%7C%7C%7C%7C%2Fg%2Felectronics%2Flarge-appliances%2Fair-conditioners/reco-v2%7C24838%7C1%7C%7C00000001C5440A8A6BC8E0297C11F2B8E72C1916%7C', "paytm"],
		# ['https://paytm.com/shop/p/videocon-vsn33wv2-3-star-1-ton-split-ac-LARVIDEOCON-VSNBANG26861773BC6CDD?src=grid&tracker=%7C%7C%7C%7C%2Fg%2Felectronics%2Flarge-appliances%2Fair-conditioners/reco-v2%7C24838%7C1%7C%7C00000001C5440A8A6BC8E0297C11F2B8E72C1916%7C', "paytm"],
		# ['https://paytm.com/shop/p/ifb-iacs18ka3tc-1-5-ton-3-star-split-ac-LARIFB-IACS18KASALE258075EC7BE2C5?src=grid&tracker=%7C%7C%7C%7C%2Fg%2Felectronics%2Flarge-appliances%2Fair-conditioners/reco-v2%7C24838%7C2%7C%7C00000001C5440A8A6BC8E0297C11F2B8E72C1916%7C',"paytm"],
		# ['https://paytm.com/shop/p/sony-kdl-43w800d-108cm-43-led-tv-full-hd-LARSONY-KDL-43WBEST182943E8D29DD4?src=grid&tracker=||||%2Fg%2Felectronics%2Faudio-video%2Ftelevisions/reco-v2|24843|1||000000014E57C0E78358939E8F41C4059135CE98|',"paytm"],
		# ['https://paytm.com/shop/p/lg-43lh576t-108-cm-43-led-tv-full-hd-LARLG-43LH576T-BANG2686178B3F0E0D?src=grid&tracker=||||%2Fg%2Felectronics%2Faudio-video%2Ftelevisions/reco-v2|24843|2||000000014E57C0E78358939E8F41C4059135CE98|',"paytm"],
		# ['https://paytm.com/shop/p/sony-kdl-43w950d-108cm-43-led-tv-full-hd-LARSONY-KDL-43WSONY2330508D4F73C4?src=grid&tracker=||||%2Fg%2Felectronics%2Faudio-video%2Ftelevisions/reco-v2|24843|13||000000014E57C0E78358939E8F41C4059135CE98|',"paytm"],
		# ['https://www.snapdeal.com/product/samsung-galaxy-s5-charcoal-black/899231383#bcrumbSearch:samsung%20galaxy%20s5',"snapdeal"],
		# ['https://www.snapdeal.com/product/iphone-6s-16gb-gold/623846347834#bcrumbSearch:apple%20iphone%206s',"snapdeal"],
		# ['https://www.snapdeal.com/product/lenovo-k3-note-16gb-black/627705225055#bcrumbSearch:lenovo|bcrumbLabelId:12',"snapdeal"],
		# ['https://www.snapdeal.com/product/lg-15-ton-3-star/652022196882#bcrumbLabelId:230',"snapdeal"],
		# ['https://www.snapdeal.com/product/videocon-1-ton-5-star/646904754378#bcrumbLabelId:230',"snapdeal"],
		# ['https://www.snapdeal.com/product/ifb-15-ton-3-star/1352826129#bcrumbLabelId:230',"snapdeal"],
		# ['https://www.snapdeal.com/product/sony-kdl43w800d-109-cm-43/672053439838#bcrumbSearch:sony%20bravia%20ultra%20hd%20uhd',"snapdeal"],
		# ['https://www.snapdeal.com/product/lg-43lh576t-108-cm-43/658986046777#bcrumbLabelId:64',"snapdeal"],
		# ['https://www.snapdeal.com/product/samsung-40j5100-1016-cm-40/657947891594#bcrumbLabelId:64',"snapdeal"],
		#['http://www.ebay.in/itm/Samsung-Galaxy-S5-G900H-16GB-BLACK-SEALED-PACK-PIECE-/292039926996?hash=item43feefa4d4:g:78UAAOSw~AVYqWuu',"ebay"],
		# ['http://www.ebay.in/itm/Apple-iPhone-6S-Latest-Model-16GB-Gold-Smartphone-/222427104429?hash=item33c9b044ad:g:fRIAAOSwax5YsCzi',"ebay"],
		# ['http://www.ebay.in/itm/Lenovo-K3-Note-BLACK-PROMO-/222423562697?hash=item33c97a39c9:g:eUAAAOSwCU1YpE4I',"ebay"],
		# ['http://www.ebay.in/itm/LG-SMART-Inverter-Split-AC-1-5Ton-Air-Conditioner-Brand-New-Sealed-VAT-Bill-/152427954534?hash=item237d6a0166:g:OaEAAOSwcUBYIGvC',"ebay"],
		# ['http://www.ebay.in/itm/Videocon-VSN33-WV2-MDA-SDA-SDM-Split-AC-1-Ton-3-Star-Rating-White-Aluminium-/262872296435?hash=item3d3468ebf3:g:M~kAAOSwXYtYs-ed',"ebay"],
		# ['http://www.ebay.in/itm/IFB-Air-Conditioner-IACS18KA3TGC-1-5-Ton-3-Star-/142286644552?hash=item2120f1e548:g:D~oAAOSw32lYq9qj',"ebay"],
		# ['http://www.ebay.com/itm/Sony-KDL48R510C-48-48-Inch-Full-HD-1080p-Smart-LED-TV-2015-Model-Built-in-WiFi-/272501553775?hash=item3f725bba6f:g:Y3oAAOSwNRdX5T30',"ebay"],
		# ['http://www.ebay.com/itm/LG-43UH6107-43-quot-108-cm-quot-Smart-TV-webOS-3-0-4K-/172444939241?hash=item282684f3e9:g:lOkAAOSwnHZYUTpJ',"ebay"],
		# ['http://www.ebay.com/itm/TV-SAMSUNG-SMARTV-102cm-3D-Tres-peu-utilise-Offre-a-part-pour-la-XBOX-/222429193933?hash=item33c9d026cd:g:iOEAAOSw4A5YrbOg',"ebay"]
		]

for link in links:
	crawler = Crawl(link[0], link[1])
	data= crawler.crawl()
	print link[1]
	print data
	print data.save()

# crawler = Crawl(links[3][0], links[3][1])
# data= crawler.crawl()
# # print link[1]
# print data
# print data.save()


# insert into products(url, site,active) values('https://www.snapdeal.com/product/samsung-galaxy-s5-charcoal-black/899231383#bcrumbSearch:samsung%20galaxy%20s5','snapdeal',1)