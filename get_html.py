import http.client

inst = http.client.HTTPSConnection("www.music-expert.ru")

inst.request("GET","/")
html = inst.getresponse()
print(html.status, html.reason)