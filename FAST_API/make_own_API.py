from fastapi import FastAPI

app=FastAPI()  #make an obj
@app.get('/')
def hello():
    return{'message':'HELLO WORLD'}

