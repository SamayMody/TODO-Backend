import pymongo

import os
from dotenv import load_dotenv
load_dotenv()

MongoURI = os.getenv('MongoURL')


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

def delete(date: int , task_description: str , completed: bool):
    response = collection.delete_one({"date": date ,"task_description": task_description, "completed": completed})
    return response.deleted_count

def update(data):
    data = dict(data)
    response = collection.update_one(
        {"date": data["date"] , "task_description": data["task_description"]},
        {"$set": {

            "completed": data["completed"]

        }}
    )
    return response.modified_count

