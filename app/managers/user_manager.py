from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Type, Any
from app.managers.base_manager import BaseManager
from app.services.user_service import UserService
from app.auth.core.security import hash_password
from app.db.models.user import User
from app.config.config import Messages

class UserManager(BaseManager[User, UserService]):
    service = UserService
    
    @staticmethod
    async def get_user_by_username_or_404(db: AsyncSession, username: str) -> User:
        user = await UserService.get_by_username(db, username)
        if not user:
            raise HTTPException(status_code=404, detail=Messages.USER_NOT_FOUND)
        return user

    @staticmethod
    async def get_user_by_email_or_404(db: AsyncSession, email: str) -> User:
        user = await UserService.get_by_email(db, email)
        if not user:
            raise HTTPException(status_code=404, detail=Messages.USER_NOT_FOUND)
        return user

    @staticmethod
    async def update_user(db: AsyncSession, user_id: int, data: dict) -> User:
        user = await UserManager.get_or_404(db, user_id)

        if "username" in data and data["username"] != user.username:
            await UserManager.check_username(db, data["username"])

        if "email" in data and data["email"] != user.email:
            await UserManager.check_email(db, data["email"])

        if "password" in data:
            data["password"] = hash_password(data["password"])

        updated_user = await UserService.update(db, user_id, data)
        if not updated_user:
            raise HTTPException(status_code=400, detail=Messages.USER_UPDATE_ERROR)

        await db.commit()
        return updated_user

    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int) -> dict:
        user = await UserManager.get_or_404(db, user_id)
            
        await UserService.delete(db, user)
        await db.commit()
        return {"detail": Messages.USER_DELETE_SUCCESS}
    
    @staticmethod
    async def get_by_user_id_or_404(db: AsyncSession, user_id: int, cls: Type[Any]) -> Any:
        user = await UserService.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail=Messages.USER_NOT_FOUND)

        result = await db.execute(select(cls).where(cls.user_id == user.id))
        obj = result.scalar_one_or_none()

        if not obj:
            raise HTTPException(status_code=404, detail=Messages.GENERIC_NOT_FOUND)

        return obj

    @staticmethod
    async def check_username(db: AsyncSession, username: str) -> None:
        existing = await UserService.get_by_username(db, username)
        if existing:
            raise HTTPException(status_code=400, detail=Messages.USERNAME_ALREADY_REGISTERED)

    @staticmethod
    async def check_email(db: AsyncSession, email: str) -> None:
        existing = await UserService.get_by_email(db, email)
        if existing:
            raise HTTPException(status_code=400, detail=Messages.EMAIL_ALREADY_REGISTERED)
