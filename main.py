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
def delete(date: int , completed: bool):
    data = database.delete(date , completed)
    return {"deleted": True , "deleted_count": data}


@app.get("/completion_percentage")
def get_completion_percentage(date: int):
    # Get all tasks for the specified date
    tasks = database.get_oneWholeDayTasks(date)

    if isinstance(tasks, list):
        total_tasks = len(tasks)
        completed = sum(1 for task in tasks if task.get("completed", False))

        if total_tasks > 0:
            percentage_completed = (completed / total_tasks) * 100
        else:
            percentage_completed = 0

        return {"date": date, "completion_percentage": percentage_completed}
    else:
        return {"date": date, "completion_percentage": 0}

