from fastapi import APIRouter,Depends
from app.schemas import User,UserId
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

usuarios = []

@router.get("/")
def obtener_usuarios(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    if(len(data) == 0):
        return {"Vacio":"La base de datos esta vacia"}
    return usuarios
@router.post("/create_user")
def crear_usuario(user:User,db:Session = Depends(get_db)):
    useer = user.dict()
    new_user = models.User(
        name= useer["name"],
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

@router.post("/{user_id}")
def obtener_usuario(user_id:int):
    for user in usuarios:
        if(user["id"] == user_id):
            return {"Exito":f"Usuario encontrado{user}"}
    return {"Error":"Usuario no encontrado"}

@router.post("/")
def obtener_usuario2(user_id:UserId):
    for user in usuarios:
        if(user["id"] == user_id.id):
            return {"Exito":f"Usuario encontrado{user}"}
    return {"Error":"Usuario no encontrado"}

@router.delete("/{user_id}")
def delete_user(user_id:int):
    for index,user in enumerate(usuarios):
        if(user["id"] == user_id):
            usuarios.pop(index)
            return {"Exito":"Usuario eliminado correctamente"}
    return {"Error":f"El usuario con el id: {user_id} no existe"}


@router.put("/{user_id}")
def update_user(user_id:int,updateUser:User):
    for index,user in enumerate(usuarios):
        if(user["id"] == user_id):
            usuarios[index]['id'] = updateUser.dict()["id"]
            usuarios[index]['name'] = updateUser.dict()["name"]
            usuarios[index]['surname'] = updateUser.dict()["surname"]
            usuarios[index]['username'] = updateUser.dict()["username"]
            usuarios[index]['password'] = updateUser.dict()["password"]
            usuarios[index]['number_phone'] = updateUser.dict()["number_phone"]
            usuarios[index]['mail'] = updateUser.dict()["mail"]
            return {"Exito":"Usuario actualizado correctamente"}
    return {"Error":f"El usuario con el id: {user_id} no existe"}