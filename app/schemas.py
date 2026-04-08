from pydantic import BaseModel,EmailStr

class CreateCategory(BaseModel):
    
    cat_name:str
   

class CreateExpense(BaseModel):
    exp_name:str
    exp_ammount:int
    category_id:int
    
class CreateUser(BaseModel):
    email:EmailStr
    password:str

class Login(BaseModel):
    email:EmailStr
    password:str
    
class ResponseCategory(CreateCategory):
    id:int
    
    class Config:
        from_attributes = True
    

class ResponseExpense(CreateExpense):
    exp_id:int

    class Config:
        from_attributes = True

class ResponseUser(CreateUser):
    email:EmailStr

    class Config:
        from_attributes=True
    