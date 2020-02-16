from sqlalchemy import *

class sqlAlchemyConnection:

	def createConnection(self,setting_ob):

		DRIVER = "ODBC Driver 17 for SQL Server"

		self.Database_Connection = f'mssql://{setting_ob.USERNAME}:{setting_ob.SECRET}@{setting_ob.SERVER}/{setting_ob.DATABASE}?driver={DRIVER}' 

		try:
			self.engine = create_engine(self.Database_Connection)
			print("Connected Successfully !!!")
			
			return self.engine

		except:
			print("ERROR in Connection !!!")
