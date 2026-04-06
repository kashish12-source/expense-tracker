from fastapi import FastAPI, HTTPException,Depends
from sqlalchemy.orm import Session
from .import models,schemas,crud
from .database import SessionLocal,engine
models.Base.metadata.create_all(bind=engine)


app=FastAPI()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/",response_model=schemas.ResponseCategory)
def post_category(user:schemas.CreateCategory,db:Session=Depends(get_db)):
    return crud.create_category(db,user)
    
@app.post("/users/",response_model=schemas.ResponseExpense)
def post_expense(user:schemas.CreateExpense,db:Session=Depends(get_db)):
    return crud.create_expense(db,user)

@app.get("/user/{id}")
def get_category(id:int , db:Session=Depends(get_db)):
    user= crud.get_category(db,id)
    if user is None:
        raise HTTPException(status_code=404,detail="id not found")

    return user

@app.get("/users/{id}")
def get_expense(id:int , db:Session=Depends(get_db)):
    user=crud.get_expense(db,id)
    if user is None:
        raise HTTPException(status_code=400,detail="id not found")
    return user

@app.delete("/user/{id}")
def delete_category(id:int ,db:Session=Depends(get_db)):
    user=crud.delete_category(db,id)
    if user is None:
        raise HTTPException(status_code=400,detail="id not found")
    return user

@app.delete("/users/{id}")
def delete_expense(id:int ,db:Session=Depends(get_db)):
    user=crud.delete_expense(db,id)
    if user is None:
        raise HTTPException (status_code=404,detail="id not found")
    return user

@app.put("/user/{id}",response_model=schemas.ResponseCategory)
def update_category(id:int,user:schemas.CreateCategory ,db:Session=Depends(get_db)):
    user=crud.update_category(db,id,user)
    if user is None:
        raise HTTPException(status_code=400,detail="id is not found")

    return user

@app.put("/users/{id}",response_model=schemas.ResponseExpense)

def update_exp(id:int ,user:schemas.CreateExpense,db:Session=Depends(get_db)):
    db_update=crude.update_expense(db,id,user)
    if db_update is None:
        raise HTTPException(status_code=404,detail="id not found")
    db_update.exp_name=user.exp_name
    db_update.exp_ammount=user.exp_ammount
    db_update.category_id=user.category_id
    db.commit()
    db.refresh(db_update)
    return db_update