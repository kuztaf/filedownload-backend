from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])


# Simulación de base de datos
fake_users_db = []

# Crear usuario
@router.post("/", response_model=User)
def create_user(user: User):
    fake_users_db.append(user)
    return user

# Obtener todos los usuarios
@router.get("/", response_model=List[User])
def get_users():
    return fake_users_db

# Obtener usuario por ID
@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in fake_users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Actualizar usuario
@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for idx, user in enumerate(fake_users_db):
        if user.id == user_id:
            fake_users_db[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Eliminar usuario
@router.delete("/{user_id}")
def delete_user(user_id: int):
    for idx, user in enumerate(fake_users_db):
        if user.id == user_id:
            del fake_users_db[idx]
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")