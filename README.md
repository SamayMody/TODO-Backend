

## Short description: 
I have created a simple **CRUD** application using Fastapi which is a trendy python framework along with Mongodb database.This backend application **creates,reads,updates,deletes and displays completion %** of tasks set by the user . 

## Why Fastapi and mongodb 🤔 :  
**FastAPI** is built for Python, which is known for its simplicity and readability.It is known for its high performance due to its use of asynchronous programming and it is designed to handle high-concurrency scenarios efficiently.FastAPI automatically generates interactive API documentation using tools like Swagger UI.<br>
**MongoDB** is designed to scale horizontally across multiple servers and machines, allowing you to handle large amounts of data and high traffic loads. It supports sharding, which distributes data across multiple servers, and replication, which provides high availability and fault tolerance.

## Dependencies:
* pip install fastapi
* pip install python-dotenv
* pip install pymongo
* pip install pydantic
* Install MongoDb community edition and MongoDb compass

##  Now i will give a short explanation on what each file function is! 🤓

### database.py:
This code snippet is a standalone Python script that directly interacts with a MongoDB database using PyMongo.It defines functions to perform CRUD (Create, Read, Update, Delete) operations directly on the MongoDB collection.

### modal.py: 
If we try posting anything then the **Swagger UI** will demand for it in querry format which we don't want we only need certain data from the user, so we create this file where a class is mentioned in which there are attributes such as  **date , task_description , completed**.

### main.py:
This code snippet defines route handlers that respond to HTTP requests made to specific endpoints.
The functions in this snippet are higher-level and are responsible for handling incoming HTTP requests and delegating database operations to another module (db1).
It uses FastAPI decorators like @app.get, @app.post, etc., to associate functions with specific HTTP methods and endpoints.

### requirements.txt:
This file contains all the dependencies required to run this project!
Just copy this file into your project and run 
```
pip install -r requirements.txt
```

## Steps to implement this project 😉 : 
- Copy the files in your IDE or text editor.
- run the following to install the dependencies ``` pip install -r requirements.txt ``` .
- Create your own MongoDB cluster. Now you would have to connect your MongoDB cluster with your code using the link provided by Mongodb which contains your username and password
- The variable "**MongoURI**" in the **database.py** file has my cluster link in the form of os.getenv('MongoURL')
- Now "**MongoURL**" is another variable having my cluster connection link in the **.env** file that is created to store sensitive information such as the cluster connection link.
- The **.env** file in this repository is just an example of what it should contain to run this project. Replace the example link with your actual cluster connect link.
- Run the below command in your terminal :
 ```
uvicorn main:app --reload
```
- Open the following link to test the api [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

 ## Output Screenshots : 
 ![Screenshot (9)](https://github.com/SamayMody/TODO-Backend/assets/113875363/fd16dd41-8922-4847-8682-0659cf5787d3) <br>

 
![Screenshot (11)](https://github.com/SamayMody/TODO-Backend/assets/113875363/8da6b62c-a923-4e4a-aee9-f5c96046f414) <br>




# End of README!!!!!




