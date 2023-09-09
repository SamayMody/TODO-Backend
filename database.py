import pymongo

MongoURI = "mongodb+srv://samaymody:Srmsam%4033@cluster0.ri5c637.mongodb.net/"
client = pymongo.MongoClient(MongoURI)
db = client["TODO_Application"]
collection = db["Task"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

def all():
    response = collection.find({})
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def get_oneWholeDayTasks(condition):
    response = collection.find({"date": condition})
    tasks = [task for task in response]
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

def delete(date: int , completed: bool):
    response = collection.delete_one({"date" : date , "completed" : completed})
    return response.deleted_count

def update(data):
    data = dict(data)
    response = collection.update_one(
        {"date": data["date"]},
        {"$set": {
            "completed": data["completed"],
        }}
    )
    return response.modified_count

