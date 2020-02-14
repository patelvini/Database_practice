import pyodbc

# server = 'CS79-PC\\SQLEXPRESS'
# database = 'DEMO'
# username = 'vini.patel'
# password = 'vini@123'
# DATABASE='+self.__database_name+';\

class DemoConnection:

	def __init__(self,settings):
		self.__database_name = database_name

	def createConnection(self):

		self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
								SERVER='+self.__server_host+';\
								DATABASE='+self.__database_name+';\
								UID='+self.__username+';\
								PWD='+self.__password+';\
								Trusted_Connection=yes;\
								autocommit = True;')
		print("Connected successfully")
		return self.conn.cursor()




