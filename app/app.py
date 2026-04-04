
from fastapi import FastAPI,Depends, HTTPException
from . import schemas,models
from .database import engine ,SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/category/")
def create_category(category:schemas.CreateCategory,db:Session=Depends(get_db)):
    new_category=models.Category(category_name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@app.get("/category/")
def read_category(db:Session=Depends(get_db)):
    


    return db.query(models.Category).all()
    
@app.post("/expenses/")
def create_expense(expense:schemas.CreateExpense,db:Session=Depends(get_db)):
    new_expense=models.Expenses(**expense.dict())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@app.get("/expenses/")
def get_expense(db:Session=Depends(get_db)):
    return db.query(models.Expenses).all()


@app.put("/expenses/{id}")
def update_expenses(id:int , expense:schemas.CreateExpense,db:Session=Depends(get_db)):
    if id is None:
        raise HTTPException(status_code=404,detail="id is required to update the expenses")
    up=db.query(models.Expenses).filter(models.Expenses.expense_id==id).first()
    up.expense_title=expense.title
    up.expense_amount=expense.amount   
    up.category_id=expense.category_id
    db.commit()
    return{"message":"expenses are updated"}

@app.delete("/expenses/{id}/")
def delete_expense(id:int , db:Session=Depends(get_db)):
    if id is None:
        raise HTTPException(status_code=404,detail="id is required")
    exp=db.query(models.Expenses).filter(models.Expenses.expense_id==id).first()
    db.delete(exp)
    db.commit()
    
