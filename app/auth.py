from jose import jwt,JWTError
from datetime import datetime ,timedelta
from fastapi.security import OAuth2PasswordBearer 
from fastapi import Depends,HTTPException

# add password hashing


SECRET_KEY="your_secret"
ALGORITHMS="HS256"
ACCESS_TOKEN_EXPIRE_TIME=30

# CREATE TOKEN
def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=30)
    to_encode.update({"exp":expire})
    return jwt.encode( to_encode,SECRET_KEY,algorithm=ALGORITHMS)

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")
def verify_token(token:str=Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHMS])
        email: str = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return email

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
