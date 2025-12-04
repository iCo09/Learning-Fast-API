from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"data" : {"name" : "Rahul"}}

@app.get("/about")
def about():
    return {"data" : "About"} 


#{id} path parameter
@app.get("/blog/{id}")
def blog(id: int):
    return {"data" : id}

 

#http://127.0.0.1:8000/blog?limit=50  http://127.0.0.1:8000/blog?limit=50&published=true

#Query parameters
@app.get("/blog1")
def limit(limit,published: bool):
    if published:
        return {"data" :  f'{limit} blogs from the published db'}
    return {"data" :  f'{limit} blogs from the db'}




class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None

@app.post("/blog")
def create_blog(blog : Blog):
    return {"data" : f"Blog is created as title {blog.title}"} 