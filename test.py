
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://annaelsaluiz:MongoDBdeployment1@cluster0.key8g5a.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


#database
mydb= client['mydatabase']

#list all the database
client.list_database_names()

mycol=mydb['myfirstcollection']

myfirstrecord = {'fname':'Anna Elsa','lname':'Luiz','address':'Kochi'}
mycol.insert_one(myfirstrecord)

mysecrecord = {'fname':'Amanda','lname':'Luiz','address':'Kochi'}
mycol.insert_one(mysecrecord)

mythirdrecord = {'fname':'Amutha','lname':'Sunil','address':'TVM','Salary':50000}
mycol.insert_one(mythirdrecord)

multiplerecords=[
    {'ID':1,'fname':'Bayana','lname':'harris','address':'Kollam','Salary':50000},
    {'ID':2,'fname':'Amala','lname':'Sunil','address':'TVM','Salary':60000},
    {'ID':2,'fname':'devika','lname':'Jayaprakash','address':'ALP','Salary':45000},
    {'ID':3,'fname':'Sadhika ','lname':'antony','address':'PLK','Salary':22000},
    {'ID':4,'fname':'Zaigam','lname':'Fathima','address':'MLP','Salary':70000},
    {'ID':5,'fname':'Zajira','lname':'P A','address':'KZK','Salary':30000}

    ]

x= mycol.insert_many(multiplerecords)
print(x.inserted_ids)

print(mycol.find_one())

for x in mycol.find():
    print(x)


mycol.find_one({"fname":"Anna Elsa"})

mycol.find({'fname':'Amanda'})

for x in mycol.find().sort("fname",-1):
    print(x)


mycol.delete_one({'fname':'Bayana'})