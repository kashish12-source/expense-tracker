
from sqlalchemy.orm import Session
from . import models,schemas

def create_category(db:Session,user:schemas.CreateCategory):
    db_user=models.Category(cat_name=user.cat_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_expense(db:Session,user:schemas.CreateExpense):
    db_user=models.Expense(exp_name=user.exp_name,exp_ammount=user.exp_ammount,category_id=user.category_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_expense(db:Session,id:int):
    return db.query(models.Expense).filter(models.Expense.exp_id==id).first()

def get_category(db:Session,id:int):
    return db.query(models.Category).filter(models.Category.id==id).first()

def delete_category(db:Session,id:int):
    db_user=db.query(models.Category).filter(models.Category.id==id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def delete_expense(db:Session,id:int):
    db_user=db.query(models.Expense).filter(models.Expense.exp_id==id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def update_category(db:Session,id:int,user:schemas.CreateCategory):
    db_user=db.query(models.Category).filter(models.Category.id==id).first()
    if db_user:
        db_user.cat_name=user.cat_name
        db.commit()
        db.refresh(db_user)
    return db_user
def update_expense(db:Session,id:int,user:schemas.CreateExpense):
    db_user=db.query(models.Expense).filter(models.Expense.exp_id==id).first()
    if db_user:
        db_user.exp_name=user.exp_name
        db_user.exp_ammount=user.exp_ammount
        db_user.category_id=user.category_id
        db.commit()
        db.refresh(db_user)
    return db_user

