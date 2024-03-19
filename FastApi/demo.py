from fastapi import FastAPI,Query,Depends
from sqlalchemy import Column,String,Integer
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("mysql://root:@localhost:3306/kishan")

session = sessionmaker(bind=engine)

base=declarative_base()

import uvicorn
app=FastAPI()
db=session()

class User(base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(255),unique=True,index=True)
    

class UserSchema(BaseModel):
    id:int
    name:str
    class Config:
        orm_model=True


base.metadata.create_all(bind=engine)

@app.post("/create-user")
def create_User(userSchema:UserSchema):
    user=User(id=userSchema.id,name=userSchema.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get('/users')
def users_list():
   recs = db.query(User).all()
   return recs

@app.get('/user{id}')
def get_user(id:int):
   recs = db.query(User).all()
   return recs

if __name__ == "__main__":
   uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)