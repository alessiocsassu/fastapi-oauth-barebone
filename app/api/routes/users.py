from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.session import get_db
from app.schemas.user import UserRead, UserUpdate
from app.managers.user_manager import UserManager
from app.auth.core.security import get_current_user
from app.db.models.user import User
from app.config.config import Messages

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserRead)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserRead, status_code=status.HTTP_200_OK)
async def update_me(
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = await UserManager.update_user(
        db,
        current_user.id,
        user_update.dict(exclude_unset=True)
    )
    return updated

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_me(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    await UserManager.delete_user(db, current_user.id)
    return None

@router.get("/", response_model=List[UserRead])
async def list_users(
    db: AsyncSession = Depends(get_db)
):
    return await UserManager.get_all(db)

@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await UserManager.get_or_404(db, user_id)


@router.put("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await UserManager.update_user(db, user_id, user_update.dict(exclude_unset=True))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    await UserManager.delete_user(db, user_id)
    return None
