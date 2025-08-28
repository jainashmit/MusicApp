import uuid
import bcrypt
from fastapi import Depends, HTTPException
from database import getdb
from models.user import UserTable
from pydantic_schemas.user_login import UserLogin
from pydantic_schemas.user_create import UserModel
from sqlalchemy.orm import Session
from fastapi import APIRouter

router = APIRouter()



@router.post('/signup' , status_code= 201)
def signup(users: UserModel , db: Session = Depends(getdb)):
    #Check is user Alreadyt Exists 
    user_db = db.query(UserTable).filter(UserTable.email == users.email).first()
    if user_db:
        raise HTTPException(status_code= 400 , detail = 'User with same email already exists!')
    #add User
    hashed_pw = bcrypt.hashpw(users.password.encode() , bcrypt.gensalt())
    user_db = UserTable(id = str(uuid.uuid4()) , name = users.name , email = users.email , password = hashed_pw)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db


@router.post('/login')
def login(user: UserLogin , db: Session = Depends(getdb)):
    #check if user present
    user_db = db.query(UserTable).filter(UserTable.email == user.email).first()
    if not user_db:
        raise HTTPException(400, detail='Wrong Email')
    
    is_match = bcrypt.checkpw(user.password.encode() , user_db.password)
    if not is_match:
        raise HTTPException(402, detail='Wrong Password')

    return user