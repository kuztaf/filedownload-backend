from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel

from api.entites.user import User, UserCreate, UserPublic, UserUpdate
from api.db.database import SessionLocal, session_dep

router = APIRouter(prefix="/users", tags=["users"])


# Crear usuario
@router.post("/", response_model=UserPublic)
def create_user(user: UserCreate, session: session_dep):
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

# Obtener todos los usuarios
@router.get("/", response_model=List[User])
def read_users(session: session_dep):
    return session.query(User).all()

# Obtener usuario por ID
@router.get("/{user_id}", response_model=UserPublic)
def get_user(user_id: int, session: session_dep):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Actualizar usuario
@router.put("/{user_id}", response_model=UserPublic)
def update_user(user_id: int, updated_user: UserUpdate, session: session_dep):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user_data = updated_user.dict(exclude_unset=True)
        for key, value in user_data.items():
            setattr(user, key, value)
        session.commit()
        session.refresh(user)
        return user
    raise HTTPException(status_code=404, detail="User not found")
 

# Eliminar usuario
@router.delete("/{user_id}")
def delete_user(user_id: int, session: session_dep):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")