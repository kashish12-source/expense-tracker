from sqlalchemy import Column,Integer,ForeignKey,String
from .database import Base 

class Category(Base):
    __tablename__="category"
    id=Column(Integer,index=True,primary_key=True)
    cat_name=Column(String)


class Expense(Base):
    __tablename__="expense"
    exp_id=Column(Integer,primary_key=True,index=True)
    exp_name=Column(String)
    exp_ammount=Column(Integer)
    category_id=Column(Integer, ForeignKey("category.id"))



class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)