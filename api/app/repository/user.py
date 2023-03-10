from sqlalchemy.orm import Session
from app.db import models
from fastapi import HTTPException,status


def get_users(db:Session):
    data = db.query(models.User).all()
    return data

def create_user(user,db:Session):
    try:
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
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Usuario o correo ya en uso"
        )
    return {"Exito":"Usuario creado con exito"}


def get_user(user_id,db:Session):
    useer = db.query(models.User).filter(models.User.id == user_id).first()
    if (not useer):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el usuario con el id {user_id}"
        )
    return useer


def delete_user(user_id,db:Session):
    useer = db.query(models.User).filter(models.User.id == user_id)
    if (not useer.first()):
        return {"Error": f"El usuario con el id: {user_id} no existe"}
    useer.delete(synchronize_session=False)
    db.commit()
    return {"Exito":"Usuario eliminado correctamente"}


def update_user(user_id,db:Session,updateUser):
    useer = db.query(models.User).filter(models.User.id == user_id)
    if (not useer.first()):
        return {"Error": f"El usuario con el id: {user_id} no existe"}
    useer.update(updateUser.dict(exclude_unset=True))
    db.commit()
    return {"Exito":"Usuario actualizado correctamente"}