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

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str
    
    
class ResponseCategory(CreateCategory):
    id:int
    
    class Config:
        from_attributes = True
    

class ResponseExpense(CreateExpense):
    exp_id:int

    class Config:
        from_attributes = True


    