import psycopg2

try:
    conn = psycopg2.connect(database = 'shop', user = 'admin1', host = "127.0.0.1", password = '1')
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()

try:
	cur.execute("SELECT* FROM testtb")
except:
	print ("i can't SELECT")

f = cur.fetchall()
print(f)