import psycopg2

def bd_insert(db_name,atr_val1,atr_val2,atr_name1,atr_name2):
	out_str = "INSERT INTO "+ db_name +"("+ atr_name1 +","+ atr_name2 +") "
	out_str += "VALUES" + "(" + atr_val1 + "," + atr_val2 + ")"
	print(out_str)

bd_insert("testtb","'item1'","50","name","price")	