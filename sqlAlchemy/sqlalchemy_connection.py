from sqlalchemy import *

class sqlAlchemyConnection:

	def __init__(self,database_name):
		self.database_name = database_name

	def selectServerHost(self,server_host):
		self.server_host = server_host

	def selectUsername(self,username):
		self.username = username

	def selectPassword(self,password):
		self.password = password

	def createConnection(self):

		self.Database_Connection = f'mssql://{self.username}:{self.password}@{self.server_host}/{self.database_name}?driver={"SQL Server Native Client 11.0"}' 

		try:
			self.engine = create_engine(self.Database_Connection)
			print("Connected Successfully !!!")
			
			return self.engine

		except:
			print("ERROR in Connection !!!")
