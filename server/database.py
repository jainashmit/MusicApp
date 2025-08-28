from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://postgres:postgres1234@localhost:5432/musicapp'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush = False , bind = engine)

def getdb(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
