<<<<<<< HEAD
from pydantic import BaseModel

class  CreateCategory(BaseModel):
    name:str
class CreateExpense(BaseModel):
    expense_title:str
    expense_amount:int
    category_id:int
=======
from sqlalchemy.engine.processors import int_to_boolean
from pydantic import BaseModel

class CreateCategory(BaseModel):
   
    name:str

class CreateExpense(BaseModel):
   
    exp_name:str
    exp_ammount:int
    category_id:int

class ResponseCategory(CreateCategory):
    id:int
    name:str

class ResponseExpense(CreateExpense):
    exp_id:int
    exp_name:str
    exp_ammount:int
    category_id:int

>>>>>>> 79c85c6 (update expense tracker)
