from fastapi import FastAPI, Depends , HTTPException
from . import models,schemas,crud
from sqlalchemy.orm import Session
from .database import SessionLocal,engine
from .utils import hashed_password,verify_password
from .auth import create_token,verify_token

# for authentication





app=FastAPI()

models.Base.metadata.create_all(bind=engine)
    

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


# part of auth
    

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

@app.post("/singup")
def singup(user:schemas.CreateUser,db:Session=Depends(get_db)):
    existing_user=db.query(models.User).filter(models.User.email==user.email).first()

    if existing_user:
        raise HTTPException(status_code=400,detail="Email already exist")
    new_user=models.User(
        email=user.email,
        password=hashed_password(user.password)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"created"}

@app.post("/login",response_model=schemas.Token)
def login(user:schemas.UserLogin,db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.email==user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@app.get("/protected")
def protecte(current_user:str=Depends(verify_token)):
    return{"message":f"hello {current_user}"}

