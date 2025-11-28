from typing import TypeVar, Generic, List, Optional, Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

T = TypeVar("T")

class BaseService(Generic[T]):
    model: Type[T]

    @classmethod
    async def get_list(cls, db: AsyncSession) -> List[T]:
        result = await db.execute(select(cls.model))
        return result.scalars().all()

    @classmethod
    async def get_by_id(cls, db: AsyncSession, obj_id: int) -> Optional[T]:
        return await db.get(cls.model, obj_id)

    @classmethod
    async def create(cls, db: AsyncSession, data: dict) -> T:
        try:
            obj = cls.model(**data)
            db.add(obj)
            await db.flush()
            await db.refresh(obj)
            return obj
        except SQLAlchemyError:
            await db.rollback()
            raise

    @classmethod
    async def update(cls, db: AsyncSession, obj_id: int, data: dict) -> Optional[T]:
        obj = await db.get(cls.model, obj_id)
        if not obj:
            return None
        for k, v in data.items():
            setattr(obj, k, v)
        try:
            await db.flush()
            await db.refresh(obj)
            return obj
        except SQLAlchemyError:
            await db.rollback()
            raise

    @classmethod
    async def delete(cls, db: AsyncSession, obj: T) -> None:
        try:
            await db.delete(obj)
            await db.flush()
        except SQLAlchemyError:
            await db.rollback()
            raise
