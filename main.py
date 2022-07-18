from re import A
import re
from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello, api!'}

@app.get('/api/')
def get_posts():
    return {'message': 'First posts'}

@app.get('/posts/')
def get_all():
    return['first item',2,True]