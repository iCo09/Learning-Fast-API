from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Test(BaseModel):
    title : str
    body : str

@app.post('/')
def create(request: Test):
    return {"data" : request}
