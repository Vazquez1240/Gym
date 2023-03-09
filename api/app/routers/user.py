from fastapi import APIRouter,Depends
from app.schemas import User,ShowUser,UpdateUSer
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/",response_model=List[ShowUser])
def obtener_usuarios(db:Session = Depends(get_db)):
    support = user.get_users(db)

    return support
@router.post("/create_user")
def crear_usuario(useer:User,db:Session = Depends(get_db)):
    support = user.create_user(useer,db)
    return support
@router.get("/{user_id}",response_model=ShowUser)
def obtener_usuario(user_id:int,db:Session = Depends(get_db)):
    support = user.get_user(user_id,db)
    return support


@router.delete("/{user_id}")
def delete_user(user_id:int,db:Session = Depends(get_db)):
    support = user.delete_user(user_id,db)
    return support


@router.patch("/{user_id}")
def update_user(user_id:int,updateUser:UpdateUSer,db:Session = Depends(get_db)):
    support = user.update_user(user_id,db,updateUser)
    return support