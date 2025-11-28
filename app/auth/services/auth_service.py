from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from app.db.models.user import User
from app.auth.core.security import verify_password, create_access_token
from app.config.config import Messages
from app.auth.schemas.auth_schema import AuthLoginResponse

class AuthService():
    @staticmethod
    async def authenticate(db: AsyncSession, username_or_email: str, password: str) -> AuthLoginResponse:
        result = await db.execute(
            select(User).where(
                (User.username == username_or_email) | (User.email == username_or_email)
            )
        )
        user = result.scalar_one_or_none()

        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=Messages.INVALID_CREDENTIALS
            )

        token = create_access_token({"sub": user.email})
        return {"access_token": token, "token_type": "bearer"}