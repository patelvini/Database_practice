from sqlalchemy import *

server = 'CS79-PC\\SQLEXPRESS'
database = 'DEMO'
DRIVER = 'SQL Server Native Client 11.0'
username = 'vini.patel'
password = 'vini@123'
Database_Connection = f'mssql://{username}:{password}@{server}/{database}?driver={DRIVER}' 


try:
	engine = create_engine(Database_Connection)
	connection = engine.connect()
	print("SUCCESS !!!")
except:
	print("ERROR !!!")

def createTable(name, *cols):

	metadata = MetaData()
	metadata.reflect(bind = engine)

	if name in metadata.tables:
		print("Table already exists !!!")

	else:
		table = Table(name,metadata, *cols)
		table.create(engine)

createTable('Table1', Column('id', Integer, primary_key = True),Column('name', String))



inspector = inspect(engine)

for _t in inspector.get_table_names():
	print(_t)

