from pydantic import BaseModel
class Task (BaseModel) :
    date: int
    task_description: str
    completed: bool = False
