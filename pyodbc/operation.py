import demo_connection as dc
import settings as sc


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

	def createTable(self):
		table_name = input("Enter table name : ")

		query = "CREATE TABLE "+table_name+"(ID INT PRIMARY KEY IDENTITY (1,1), "

		while True:
			colname=input("Enter column name, exit to stop adding columns : ")
			if colname=="exit":
				query+=");"
				break
			dtype=input("Enter column data type: INT,CHAR OR VARCHAR : ")
			if dtype=="INT":
				query+=colname+" "+dtype+", "
			else:
				size=input("Enter size for column : ")
				query+=colname+" "+dtype+" ("+size+"), "

		cr.execute(query)
		db.conn.commit()

		print("Table created Successfully !!")

	def viewTableMetaData(self):

		table_name = input("Enter table name : ")
		query = "SELECT c.name, t.Name, ISNULL(i.is_primary_key, 0) FROM sys.columns c INNER JOIN sys.types t ON c.user_type_id = t.user_type_id LEFT OUTER JOIN sys.index_columns ic ON ic.object_id = c.object_id AND ic.column_id = c.column_id LEFT OUTER JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id WHERE c.object_id = OBJECT_ID('"+table_name+"')"
		
		res = cr.execute(query)
		print("\nColumn Name","Datatype","Is primary key", sep= " - ")
		print('\n')
		for row in res:
			print(row)
		db.conn.commit()
		

	# def updateData(self):
	# 	table_name = input("Enter table name : ")
	# 	id = input("Enter id for search : ")

if __name__ == '__main__':

	op = Operation()
	setting_ob = sc.Settings()
	db = dc.DemoConnection()
	cr = db.createConnection(setting_ob)
	op.viewTableMetaData()


	


