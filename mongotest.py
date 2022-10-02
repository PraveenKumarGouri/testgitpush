import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:1234567890@cluster0.feqyekh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d= {"name" : "praveen",
    "email" : "praveen39.39.39@gmail.com",
    "surname" : "kumar"}
db1= client['mongotest']
coll = db1['test']
coll.insert_one(d)

