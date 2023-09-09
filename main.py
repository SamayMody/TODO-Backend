from fastapi import FastAPI
import database
import modal

app = FastAPI()

@app.get("/all tasks")
def get_all():
    data = database.all()
    return {"data" : data}

@app.get("/todays tasks")
def get_one(date: int):
    data = database.get_oneWholeDayTasks(date)
    return {"data":data}

@app.post("/set tasks")
def post(data:modal.Task):
    id = database.create(data)
    return {"inserted": True, "inserted_id": id}

@app.put("/change status")
def update(data:modal.Task):
    data = database.update(data)
    return {"updated": True, "data": data}

@app.delete("/delete")
def delete(date: int):
    data = database.delete(date)
    return {"deleted": True , "deleted_count": data}

