from sqlalchemy.orm import Session
from app.db import models


def create_user(user,db:Session):
    useer = user.dict()
    new_user = models.User(
        name=useer["name"],
        surname=useer["surname"],
        username=useer["username"],
        password=useer["password"],
        number_phone=useer["number_phone"],
        mail=useer["mail"]
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"Exito":"Usuario creado con exito"}