from fastapi import FastAPI, Depends , HTTPException
from . import models,schemas,crud
from sqlalchemy.orm import Session
from .database import SessionLocal,engine


models.Base.metadata.create_all(bind=engine)
app=FastAPI()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.post("/category/",response_model=schemas.ResponseCategory)
def post_category(user:schemas.CreateCategory,db:Session=Depends(get_db)):
    return crud.create_category(db,user)
@app.get("/category/{id}")
def get_category(id:int ,db:Session=Depends(get_db)):
    user=crud.get_category(db,id)
    if user is None:
        raise HTTPException(status_code=400,detail="id not found")
    return user
@app.put("/category/{id}")
def update_user(id:int, user:schemas.CreateCategory, db:Session=Depends(get_db)):
    updated_user=crud.update_category(db,id, user)
    if updated_user is None:
        raise HTTPException(status_code=400,detail="id is not found")
    return updated_user
@app.delete("/category/{id}")
def delete_category(id:int ,db:Session=Depends(get_db)):
    user=crud.delete_category(db,id)
    if user is None:
        raise HTTPException (status_code=400,detail="id is not found")
    return user

@app.post("/expense/",response_model=schemas.ResponseExpense)
def post_expense(user:schemas.CreateExpense,db:Session=Depends(get_db)):
    return crud.create_expense(db,user)

@app.get("/expense/{id}")
def get_expense(id:int ,db:Session=Depends(get_db)):
    user=crud.get_expense(db,id)
    if user is None:
        raise HTTPException(status_code=400,detail="id not found")
    return user

@app.put("/expense/{id}")
def update_expese(id:int, user:schemas.CreateExpense, db:Session=Depends(get_db)):
    updated_user=crud.update_expense(db,id, user)
    if updated_user is None:
        raise HTTPException(status_code=400,detail="id not found")
    return updated_user

@app.delete("/expense/{id}")
def delete_expense(id :int , db:Session=Depends(get_db)):
    user=crud.delete_expense(db,id)
    if user is None:
        raise HTTPException (status_code=400,detail="id not found")
    return user

@app.post("/user/",response_model=schemas.ResponseUser)
def singup(user:schemas.CreateUser,db:Session=Depends(get_db)): 
    return crud.create_user(db,user)

@app.get("/user/")