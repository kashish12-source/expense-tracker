from sqlalchemy.orm import Session
from . import models,schemas
from fastapi import HTTPException
from .database import SessionLocal,engine

def create_category(db:Session,category:schemas.CreateCategory):
    new_category=models.Category(category_name=category.category_name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def read_category(id:int ,db:Session):
    if id is None:
        raise HTTPException(status_code=404 ,detail="id is required")
    if id is not db.query(models.Category.id).all():
        raise HTTPException(status_code=400,detail="id is not found")
    return db.query(models.Category).filter(models.Category.id==id).first()

def create_expense(db:Session,expense:schemas.CreateExpense):
    new_expense=models.Expenses(
        expense_title=expense.expense_title,
        expense_amount=expense.expense_amount,
        category_id=expense.category_id
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

def get_expense(id:int ,db:Session):
    if id is None:
        raise HTTPException(status_code=404 ,detail="id is required")
    if id is not db.query(models.Expenses.expense_id).all():
        raise HTTPException(status_code=400,detail="id is not found")
    return db.query(models.Expenses).filter(models.Expenses.expense_id==id).first()

def update_expenses(id:int ,expense :schemas.CreateExpense , db:Session):
    if id is None:
        raise HTTPException(status_code=404,detail="id is required to update the expenses")
    up=db.query(models.Expenses).filter(models.Expenses.expense_id==id).first()
    up.expense_title=expense.expense_title
    up.expense_amount=expense.expense_amount   
    up.category_id=expense.category_id
    db.commit()
    return{"message":"expenses are updated"}\
    
def delete_expenses(id:int ,db:Session):
    if id is None:
        raise HTTPException(status_code=404,detail="id is required")
    exp=db.query(models.Expenses).filter(models.Expenses.expense_id==id).first()
    db.delete(exp)
    db.commit() 

