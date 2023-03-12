from fastapi import APIRouter,Depends, status
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.repository import user
from app.schemas import Administrador,ShowAdmin
from app.repository import admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/obtener_admins",response_model=List[ShowAdmin],status_code=status.HTTP_200_OK)
def obtener_admin(db:Session = Depends(get_db)):
    support = admin.get_admins(db)
    return support


@router.post("/create_admin",status_code=status.HTTP_201_CREATED)
def create_admin(admiin:Administrador,db:Session = Depends(get_db)):
    support = admin.create_admin(admiin,db)
    return support