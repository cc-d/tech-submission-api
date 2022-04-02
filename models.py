from pydantic import BaseModel

from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = "243gt24gthoi3erdguohbrgohbr21gour3gou23r"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

SQLALCHEMY_DATABASE_URL = 'sqlite:///./db.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

db = SessionLocal()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user_id(username):
	user = db.query(APIUser).filter_by(username=username).first()
	return user.id

class APIUser(Base):
	__tablename__ = 'APIUsers'
	id = Column(Integer, primary_key=True)
	username = Column(String)
	password = Column(String)
	contacts = Column(Integer, ForeignKey('Contacts.id'), default=None, nullable=True)


class Contact(Base):
	__tablename__ = 'Contacts'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('APIUsers.id'))
	first = Column(String)
	last = Column(String)
	# JSON string containing number type and multiple numbers (postgres has a specific type for this)
	numbers = Column(String)
	city = Column(String)
	state = Column(String)
	zip_code = Column(Integer)