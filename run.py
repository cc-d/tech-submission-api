from typing import Optional

from fastapi import FastAPI

from fastapi.responses import PlainTextResponse, RedirectResponse

import uvicorn

from flask_sqlalchemy import SQLAlchemy

import json

from models import *

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def index():
    '''
    The index page of this app should print all users and any information that should be displayed
    as part of this technical submission
    '''
    users = db.query(APIUser).all()
    user_string = 'Users: '

    contacts = db.query(Contact).all()
    contact_string = 'Contacts: '

    for u in users:
        user_string += str(vars(u)) + ' '

    for c in contacts:
        contact_string += str(vars(c)) + ' '

    return user_string + ' >>>>>>> ' + contact_string


@app.get('/register')
async def register(username: str, password: str):
    '''
    Obviously in a real application, the username/password would not be a query string.
    I'm also not validating empty/invalid/duplicate inputs, in a real app I would.
    '''

    pass_hash = get_password_hash(password)
    new_user = APIUser(username=username, password=get_password_hash(password))
    db.add(new_user)
    db.commit()
    return {'success':'ok'}


@app.get('/add_contact')
async def add_contact(user: str, numbers: str, first: str, last: str, city: str,
                      state: str, zip_code: int):
    '''
    Same as above, if real app I would veriy integrity of data, handle edge cases, etc
    '''
    uid = get_user_id(user)
    new_contact = Contact(user_id=uid, numbers=numbers, first=first, last=last,
                          city=city, state=state, zip_code=zip_code)

    db.add(new_contact)
    db.commit()
    return {'success':'ok'}

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
