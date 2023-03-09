from fastapi import APIRouter,Depends
from app.schemas import User,ShowUser,UpdateUSer
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List
from app.repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/",response_model=List[ShowUser])
def obtener_usuarios(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    if(len(data) == 0):
        return {"Vacio":"La base de datos esta vacia"}
    return data
@router.post("/create_user")
def crear_usuario(useer:User,db:Session = Depends(get_db)):
    support = user.create_user(useer,db)
    return support
@router.post("/{user_id}",response_model=ShowUser)
def obtener_usuario(user_id:int,db:Session = Depends(get_db)):
    useer = db.query(models.User).filter(models.User.id == user_id).first()
    if(not useer):
        return {"Error":"Usuario no encontrado"}
    return useer


@router.delete("/{user_id}")
def delete_user(user_id:int,db:Session = Depends(get_db)):
    useer = db.query(models.User).filter(models.User.id == user_id)
    if (not useer.first()):
        return {"Error":f"El usuario con el id: {user_id} no existe"}
    useer.delete(synchronize_session=False)
    db.commit()
    return {"Exito":f"El usuario con el id: {user_id} Fue eliminado"}


@router.patch("/{user_id}")
def update_user(user_id:int,updateUser:UpdateUSer,db:Session = Depends(get_db)):
    useer = db.query(models.User).filter(models.User.id == user_id)
    if (not useer.first()):
        return {"Error":f"El usuario con el id: {user_id} no existe"}
    useer.update(updateUser.dict(exclude_unset=True))
    db.commit()

    return {"Exito":f"El usuario con el id: {user_id} fue actualizado"}