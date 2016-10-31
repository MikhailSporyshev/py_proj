import urllib.request
import re
import psycopg2

def get_names_prices(URL, names_RE, prices_RE):
	inst = urllib.request.urlopen(URL).read().decode("utf-8")

	text = inst.split("\n")
	prices = []
	names = []
	for st in text:
		n = re.search(names_RE, st)
		p = re.search(prices_RE, st)
		if n:
			names.append(n.group(2))
		if p :
			prices.append(p.group(2))
	return names, prices

def insert_names_prices(dbname, username, host_url, userpass, tablename, names, prices):
	try:
	    conn = psycopg2.connect(database = dbname, user = username, host = host_url, password = userpass)
	except:
	    print ("I am unable to connect to the database")
	    return False
	
	cur = conn.cursor()

	for name, price in zip(names,prices):
		query = 'INSERT INTO ' + tablename + '(name,price) ' + 'VALUES' + '(\'' + name + '\',' + price +')'
		try:
			cur.execute(query)
		except:
			print ("i can't INSERT")
 
	conn.commit()


if __name__ == '__main__':
	URL = "http://www.music-expert.ru/index.php?categoryID=7667&onpage=100"
	names_RE = "(<a  href=\'/index\.php\?productID=\d*\'>)(.*)(</a>)"
	prices_RE = "(<input class=\"product_price\" value=\")(\d*)(\" type=\"hidden\">)" 

	dbname = 'shop' 
	username = 'admin1' 
	userpass = '1'
	host_url = '127.0.0.1'
	tablename = 'testtable'

	names,prices = get_names_prices(URL,names_RE,prices_RE)
	insert_names_prices(dbname, username, host_url, userpass, tablename, names, prices)




