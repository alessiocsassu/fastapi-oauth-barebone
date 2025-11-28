from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, TypeVar, Generic, List
from app.services.base_service import BaseService
from app.config.config import Messages
from app.schemas.base import BaseDelete

T = TypeVar("T")
S = TypeVar("S", bound=BaseService)

class BaseManager(Generic[T, S]):
    service: Type[S]

    @classmethod
    async def get_or_404(cls, db: AsyncSession, obj_id: int) -> T:
        obj = await cls.service.get_by_id(db, obj_id)
        if not obj:
            raise HTTPException(status_code=404, detail=Messages.GENERIC_NOT_FOUND)
        return obj

    @classmethod
    async def get_all(cls, db: AsyncSession) -> List[T]:
        return await cls.service.get_list(db)

    @classmethod
    async def create(cls, db: AsyncSession, data: dict) -> T:
        try:
            return await cls.service.create(db, data)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @classmethod
    async def update(cls, db: AsyncSession, obj_id: int, data: dict) -> T:
        existing = await cls.service.get_by_id(db, obj_id)
        if not existing:
            raise HTTPException(status_code=404, detail=Messages.GENERIC_NOT_FOUND)

        updated = await cls.service.update(db, obj_id, data)
        if not updated:
            raise HTTPException(status_code=400, detail=Messages.UPDATE_ERROR)
        return updated

    @classmethod
    async def delete(cls, db: AsyncSession, obj_id: int) -> BaseDelete:
        obj = await cls.service.get_by_id(db, obj_id)
        if not obj:
            raise HTTPException(status_code=404, detail=Messages.GENERIC_NOT_FOUND)
        await cls.service.delete(db, obj)
        return {"detail": Messages.DELETE_SUCCESS}
