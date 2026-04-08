from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
# Breakdown:
# "bcrypt" → secure hashing algorithm 🔒
# deprecated="auto" → automatically handles old hashing methods


def hash_password(password:str):
    
    return pwd_context.hash(password)
    

def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

# Takes plain password (e.g. "123456")
# Converts it into a hashed password

# 👉 bcrypt is:

# Slow hashing algorithm (good for security)
# Protects against brute-force attacks
# Adds salt automatically