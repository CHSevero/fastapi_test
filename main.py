from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from authentication import Token, authenticate_user, create_access_token, User, get_current_active_user

from database import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, fake_users_db

import requests

app = FastAPI()

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
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


@app.post("/post_endpoint")
async def post_endpoint(user: str, order: float, previousOrder: bool, current_user: User = Depends(get_current_active_user)):
    return {"user": user, "order": order, "previousOrder": previousOrder}

@app.get("/get_endpoint")
async def get_endpoint(current_user: User = Depends(get_current_active_user)):
    request = requests.get('https://api.openbrewerydb.org/breweries/')
    bears_list = [bear['name'] for bear in request.json()]
    return {"bears": bears_list}