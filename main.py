from fastapi import FastAPI
import db
import models


app=FastAPI()

@app.get('/all')
def get_all():
    data = db.all()
    return {"data":data}

@app.post('/create')
def create(data:models.todo):
    id = db.create(data)
    return {"inserted":True , "inserted_id":id}

@app.get('/get/{task}')
def get_one(task:str):
    data = db.get_one(task)
    return {"data":data}


@app.delete('/delete/{task}')
def delete_task(task:str):
    response=db.delete(task)
    return {"deleted":response}

@app.put('/update')
def update_task(data:models.todo):
    data = db.update(data)
    return {"updated":data}