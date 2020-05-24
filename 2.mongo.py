from pymongo import MongoClient

client = MongoClient('localhost', 27107)
db = client.test
collection = db.users

print(db.name)

collection.insert_many([{
  'name': '李金珂',
  'age': 18
},{
  'name': '赵日天',
  'age': 230
}])