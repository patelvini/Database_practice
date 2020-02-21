import sqlalchemy as db

server = 'CS79-PC\\SQLEXPRESS'
database = 'DEMO'
DRIVER = 'SQL Server Native Client 11.0'
username = 'vini.patel'
password = 'vini@123'
Database_Connection = f'mssql://{username}:{password}@{server}/{database}?driver={DRIVER}' 
engine = db.create_engine(Database_Connection)
connection = engine.connect()

metadata = db.MetaData()

result = db.Table('CUSTOMER1', metadata, autoload = True, autoload_with = engine)

print("\n",result.columns.keys(),"\n") 

print(repr(metadata.tables['CUSTOMER1']))

query = db.select([result])

resultProxy = connection.execute(query)

resultSet = resultProxy.fetchall()

print("\n",resultSet,"\n")

r1 = db.select([result]).where(result.columns.FIRST_NAME=='Vini')

res = connection.execute(r1)

for i in res:
	print(i)


q2 = db.Table('CUSTOMER5', metadata, db.Column('id',db.Integer, primary_key = True), db.Column('name', db.String), db.Column('lastname',db.String))

# # q2 = db.Table('CUSTOMER6', metadata, db.Column('id', db.Integer, primary_key = True, ))

# metadata.create_all(engine)

# # print(q2.columns.keys())

# col = db.Column('col1', db.String)

# col.create('CUSTOMER6',engine)

# print(q2.columns.keys())






