<<<<<<< HEAD
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

=======
from sqlalchemy import Column ,Integer,String,ForeignKey,PrimaryKeyConstraint
from .database import Base, engine

class Category(Base):
    __tablename__="cat"
    id=Column(Integer,primary_key=True,index=True) 
    name=Column(String)

class Expense(Base):
    __tablename__="exp"
    exp_id=Column(Integer,primary_key=True,index=True)
    exp_name=Column(String)
    exp_ammount=Column(Integer)
    category_id=Column(Integer, ForeignKey("cat.id"))
>>>>>>> 79c85c6 (update expense tracker)
