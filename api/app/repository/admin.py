from sqlalchemy.orm import Session
from app.db import models
from fastapi import HTTPException,status

def get_admins(db:Session):
    data = db.query(models.Administrador).all()
    return data


def create_admin(user_admin,db:Session):
    try:
        admiin = user_admin.dict()
        new_admin = models.Administrador(
            name = admiin["name"],
            surname = admiin["surname"],
            username = admiin["username"],
            password = admiin["password"],
            number_phone = admiin["number_phone"],
            mail = admiin["mail"],
            rango = admiin["rango"]
        )
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="username or mail already in use"
        )
    return {"Success":"Admin create with exit!"}

def get_admin(user_admin, db:Session):
    admiin = db.query(models.Administrador).filter(models.Administrador.username == user_admin).first()
    if(not admiin):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username does not exist: {user_admin}"
        )
    return admiin


def delete_admin(user_admin, db:Session):
    admiin = db.query(models.Administrador).filter(models.Administrador.username == user_admin)
    if(not admiin.first()):
        return {"Error":f"El administrador con el username {user_admin} no existe"}
    admiin.delete(synchronize_session=False)
    db.commit()
    return {"Success":"Usuario eliminado correctamente"}