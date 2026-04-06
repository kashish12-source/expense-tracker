from sqlalchemy.orm import Session
<<<<<<< HEAD
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
=======
from . import models , schemas


def create_category(db:Session,category:schemas.CreateCategory):
    db_category=models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_expense(db:Session,exp:schemas.CreateExpense):
    db_expense=models.Expense(exp_name=exp.exp_name,exp_ammount=exp.exp_ammount,category_id=exp.category_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expense(db:Session,id:int):
    return db.query(models.Expense).filter(models.Expense.exp_id==id).first()

def get_category(db:Session,id:int):
    return db.query(models.Category).filter(models.Category.id==id).first()

def get_expense(db:Session,id:int):
    return db.query(models.Expense).filter(models.Expense.exp_id==id).first()

def delete_category(db:Session,id:int):
    db_category=db.query(models.Category).filter(models.Category.id==id).first()
    db.delete(db_category)
    db.commit()
    return db_category

def delete_expense(db:Session,id:int):
    db_expense=db.query(models.Expense).filter(models.Expense.exp_id==id).first()
    db.delete(db_expense)
    db.commit()
    return 
    
def update_category(db:Session,id:int,user:schemas.CreateCategory):
    db_update_cat=db.query(models.Category).filter(models.Category.id==id).first()
    
    db_update_cat.name=user.name
    db.commit()
    db.refresh(db_update_cat)
    return db_update_cat

def update_expense(db:Session,id:int,user:schemas.CreateExpense):
    db_update_exp=db.query(models.Expense).filter(models.Expense.exp_id==id).first()
    if id:
        db_update_exp.exp_name=user.exp_name
        db_update_exp.exp_ammount=user.exp_ammount
        db_update_exp.category_id=user.category_id
    db.commit()
    db.refresh(db_update_exp)
    return db_update_exp
>>>>>>> 79c85c6 (update expense tracker)

