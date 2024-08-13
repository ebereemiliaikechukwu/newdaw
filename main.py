from fastapi import FastAPI, Path, Query, UploadFile, Depends, Form, HTTPException, Header, Cookie

from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

#from _json import JWTError, jwt

from pydantic import BaseModel

import schemas, crud, models
from Database import engine, db_session





app =FastAPI()


models.Base.metadata.create_all(bind=engine)



# Dependency
def get_session():
    try:
        db = db_session()
        yield db
    finally:
        db.close()

@app.post("/signup")
def user(user: schemas.User, session=Depends(get_session)):
    new_user = crud.create_user(session, user)
    return new_user


#Develop a fully functional API for a personal portfolio website, including endpoints for projects (add, edit, delete,all project, single project),
#blog posts (add, edit, delete,all blog posts, single blog post), 
#and contact information (add, edit, delete

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3


app = FastAPI()




@app.post("/signup")
def user(user: schemas.User, session=Depends(get_session)):
    new_user = crud.create_user(session, user)
    return new_user



@app.post("/user")
def user(user: schemas.User, session=Depends(get_session)):
    user = crud.create_user(session, user)


    if user:
        raise HTTPException(
            status_code=404, 
            detail="user information updated"
            )




@app.post('/user')
def delete_user(user: schemas.User, session=Depends(get_session)):
    user = crud.delete_user(session, user)

    if user:
        
     raise HTTPException(
        status_code=404, 
        details="user  not found")









