import demo_connection as dc

class Operation:

	def insertData(self):
		p_name = input("Enter product name : ")
		price = input("Enter price : ")

		cr.execute("INSERT INTO PRODUCT (PRODUCT_NAME,PRICE) VALUES (?,?)",(p_name,price))
		db.conn.commit()
		print("Inserted Successfully !!\n")

		# return self.insert_data
	def readData(self):
		table_name = input("Enter table name : ")
		self.res = cr.execute("SELECT * FROM "+table_name)
		for row in self.res:
			print(row)

		db.conn.commit()

	# def updateData(self):
	# 	table_name = input("Enter table name : ")
	# 	id = input("Enter id for search : ")

if __name__ == '__main__':

	op = Operation()
	# db = dc.DemoConnection('DEMO')

	# db.selectServerHost('CS79-PC\\SQLEXPRESS')
	# db.selectUsername('vini.patel')
	# db.selectPassword('vini@123')
	db = dc.DemoConnection(input("Enter database name : "))

	db.selectServerHost(input("Enter server host name : "))
	db.selectUsername(input("Enter user name : "))
	db.selectPassword(input("Enter password : "))

	cr = db.createConnection()


	


