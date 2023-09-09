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
    for i in response :
        i["_id"] = str(i["id"])
        data.append(i)
    return data

def get_oneWholeDayTasks(condition):
    response = collection.find_one({"date" : condition})
    response["_id"] = str(response["_id"])
    return response


def delete(condition):
    response = collection.delete_one({"date" : condition})
    return response.deleted_count

def update(data):
    data = dict(data)
    response = collection.update_one(
        {"date": data["date"]},
        {"$set": {
            "completed": data["completion_status"],
        }}
    )
    return response.modified_count

