# from str import join
import psycopg2
import re

class Product:

	def __init__(self,site, url, name="", price="", rating="2.5",description=""):
		self.url = url
		self.site = site
		self.name = name
		p1 = re.findall(r'[0-9]+[\.]*[0-9]*', price)
		self.price = "".join(p1)
		p2 = re.findall( r'[0-9\.]+',rating)
		self.rating = "".join(p2)
		self.description= description
		#self.product_id= id

	def __str__(self):
		return("Name: "+self.name.encode('UTF-8')+ "\r\nPrice: "+ self.price.encode('UTF-8')+ "\r\nRating: "+ self.rating.encode('UTF-8') + "\r\nDesscription: "+ self.description.encode('UTF-8') + "\r\n" )
	def save(self):
		try:
			conn = psycopg2.connect("dbname='projectdb' user='postgres' host='localhost' password='Innova123'")
			print "connected"
		except Exception as e:
			print "Unable to connect"	
			print e
		cur = conn.cursor()
		query = "SELECT id from products where url='%s'" % self.url
		try:
			cur.execute(query)
			rows = cur.fetchall()
			print "Checking %s" % self.url
			print len(rows)
			if len(rows) == 1:
				print "product exists"
				self.product_id = rows[0][0]
			else:
				print "product doesnot exists"
				query ="INSERT INTO products(url, site, active) VALUES ('%s','%s','%s') RETURNING id" % (self.url, self.site, 1)
				cur.execute(query)
				self.product_id = cur.fetchone()[0]
				print self.product_id
		except Exception as e:
			print "connot get the product id"
			print e
		# cur.execute("select * from products")
		# rows = cur.fetchall()
		# for row in rows:
		# 	print row
		# cur.execute("select * from product_metadata")
		# rows = cur.fetchall()
		# for row in rows:
		# 	print row
		try:
			query = "INSERT INTO product_metadata(product_id, name,price,rating,description)VALUES('%s','%s','%s','%s', '%s')" % (self.product_id, self.name, self.price, self.rating,self.description)
			cur.execute(query)	
		except Exception as e:
			print "connot execute"
			print e
		conn.commit()


