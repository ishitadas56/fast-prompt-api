
from fastapi import FastApi

app=FastAPI()
@app.get('/')
def hello_world();
    return {'Hello:''World'}