from sqlalchemy import Column ,Integer,String,ForeignKey
from .database import Base

class Category(Base):
    __tablename__="category"
    id=Column(Integer ,primary_key=True,index=True)
    category_name=Column(String)

class Expenses(Base):
    __tablename__="expenses"
    expense_id=Column(Integer,primary_key=True,index=True)
    expense_title=Column(String)
    expense_amount=Column(Integer)
    category_id=Column(Integer , ForeignKey("category.id"))

