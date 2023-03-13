from sqlalchemy.orm import Session
from app.db import models
from fastapi import HTTPException,status
from datetime import datetime, timedelta
from app.hashing import Hash
from app.token import create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES

def auth_user(user,db:Session):

    useer = db.query(models.User).filter(models.User.username == user.username).first()
    print(user)
    if(not user):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el usuario con el username: {user.username}"
        )
    if(not Hash.verify_password(user.password,useer.password)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Password incorrect"
        )
    # Esto se saco de la documentacion de fastapi
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
