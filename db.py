import pymongo

mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)

db = client["todo"]
collection = db["tasks"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

def all():
    response = collection.find({},{"_id" : 0})
    return list(response)

def get_one(condition):
    response = collection.find_one({"task":condition},{"_id":0})
    return response

def update(data):
    data = dict(data)
    response = collection.update_one({"task":data["task"]}, {"$set":{"desc":data["desc"]}}) 
    return True

def delete(task):
    response = collection.delete_one({"task":task})
    return True