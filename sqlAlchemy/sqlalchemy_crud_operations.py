from sqlalchemy import *
import sqlalchemy_connection as sql_c
import settings as sc

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

	# def inserData(self,*values):
	# 	table_name = input("Enter table name : ")
	# 	self.metadata.reflect(bind = engine)

	# 	if table_name in self.metadata.tables:
	# 		result = Table(table_name, self.metadata, autoload = True, autoload_with = engine)
	# 		list1 = result.columns.keys()
	# 		print(f"Columns in table {table_name} : ",list1)

			
	# 		ins = result.insert().values()
	# 		self.connection.execute(ins)
			
	# 		print("Inserted successfully !!!")

	# 	else:
	# 		print("No table found !!!")

if __name__ == '__main__':

	setting_ob = sc.Settings()

	db = sql_c.sqlAlchemyConnection()

	engine = db.createConnection(setting_ob)

	op = sqlAlchemyOperation()

	# op.readData()
	# op.createTable(input("Enter table name : "), Column(input("Enter column name : "), Integer, primary_key = True))
	op.viewTableList()
	# op.readData()

	op.inserData()
