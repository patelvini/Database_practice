from sqlalchemy import *
import sqlalchemy_connection as sc

class sqlAlchemyOperation:

	def __init__(self):
		self.metadata = MetaData()
		self.connection = engine.connect()
		self.inspector = inspect(engine)


	def createTable(self,name,*cols):

		if name in self.metadata.tables:
			print("Table already exists !!!")

		else:
			table = Table(name,self.metadata, *cols)
			table.create(engine)
			print("Table created successfully !!!")

	def viewTableList(self):

		for t in self.inspector.get_table_names():
			print(t)

	def readData(self):

		table_name = input("Enter table name : ")
		self.metadata.reflect(bind = engine)

		if table_name in self.metadata.tables:

			result = Table(table_name, self.metadata)
			select_st = select([result])
			res = self.connection.execute(select_st)
			for row in res:
				print(row)
		else:
			print("No table found !!!")

	# def inserData(self):
	# 	table_name = input("Enter table name : ")
	# 	self.metadata.reflect(bind = engine)

	# 	if table_name in self.metadata.tables:
	# 		result = Table(table_name, self.metadata, autoload = True, autoload_with = engine)
	# 		list1 = result.columns.keys()
			
	# 		print(f"Columns in table {table_name} : ",list1)

	# 		n = int(input("Enter how many records you want to insert : "))

	# 		for i in range(0,n):
	# 			ins = (result.insert(),{list1[]})	
	# 			self.connection.execute(ins)
	# 			print("Inserted successfully !!!")		

	# 	else:
	# 		print("No table found !!!")

if __name__ == '__main__':

	# server = 'CS79-PC\\SQLEXPRESS'
	# database = 'DEMO'
	# DRIVER = 'SQL Server Native Client 11.0'
	# username = 'vini.patel'
	# password = 'vini@123'

	# db = sc.sqlAlchemyConnection(input("Enter name for database : "))

	# db.selectServerHost(input("Enter server host name : "))
	# db.selectUsername(input("Enter user name : "))
	# db.selectPassword(input("Enter password : "))

	db = sc.sqlAlchemyConnection('DEMO')
	db.selectServerHost('CS79-PC\\SQLEXPRESS')
	db.selectUsername('vini.patel')
	db.selectPassword('vini@123')
	engine = db.createConnection()

	op = sqlAlchemyOperation()

	# op.readData()
	# op.createTable(input("Enter table name : "), Column(input("Enter column name : "), Integer, primary_key = True))
	op.viewTableList()
	# op.readData()

	op.inserData()


