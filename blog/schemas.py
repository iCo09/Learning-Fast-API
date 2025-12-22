from pydantic import BaseModel

class Blog(BaseModel):
    title : str
    body : str 

class ShowBlog(BaseModel):
    title : str
    class Config():
        orm_mode = True

class User(BaseModel):
    user : str
    email : str
    password : str

class ShowUser(BaseModel):
    user : str
    email : str
    class Config():
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    scopes: list[str] = []