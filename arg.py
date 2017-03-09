
import sys
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


crawler = Crawl(sys.argv[1],sys.argv[2])
data= crawler.crawl()
print data