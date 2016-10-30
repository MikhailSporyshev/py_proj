import urllib.request
import re

inst = urllib.request.urlopen("http://www.music-expert.ru/index.php?categoryID=7667&onpage=45").read().decode("utf-8")

text = inst.split("\n")
prices = []
names = []
for st in text:
	p = re.search("(<input class=\"product_price\" value=\")(\d*)(\" type=\"hidden\">)", st)
	n = re.search("(<a  href=\'/index\.php\?productID=)(\d*)('>)(.*)(</a>)", st)
	if p :
		prices.append(p.group(2))
		print(p.group(2), end = ' ')
	if n:
		names.append(n.group(4))
		print(n.group(4))	