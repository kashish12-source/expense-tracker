from pydantic import BaseModel

class  CreateCategory(BaseModel):
    name:str
class CreateExpense(BaseModel):
    expense_title:str
    expense_amount:int
    category_id:int