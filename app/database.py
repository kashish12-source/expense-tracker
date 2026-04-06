from sqlalchemy import create_engine
<<<<<<< HEAD
from sqlalchemy.orm import declarative_base,sessionmaker
=======
from sqlalchemy.orm import sessionmaker,declarative_base
>>>>>>> 79c85c6 (update expense tracker)

DATABASE_URL="sqlite:///./test.db"

engine=create_engine(
<<<<<<< HEAD
    DATABASE_URL, connect_args={"check_same_thread":False}

)
=======
    DATABASE_URL , connect_args={"check_same_thread":False} 
    )

>>>>>>> 79c85c6 (update expense tracker)
SessionLocal=sessionmaker(bind=engine)

Base=declarative_base()