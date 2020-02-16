import pyodbc

class DemoConnection:

	def createConnection(self,setting_ob):

		self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
								SERVER='+setting_ob.SERVER+';\
								DATABASE='+setting_ob.DATABASE+';\
								UID='+setting_ob.USERNAME+';\
								PWD='+setting_ob.SECRET+';\
								Trusted_Connection=yes;\
								autocommit = True;')
		print("Connected successfully")
		return self.conn.cursor()


