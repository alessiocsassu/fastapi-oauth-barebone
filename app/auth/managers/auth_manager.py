from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.services.auth_service import AuthService
from app.auth.schemas.auth_schema import AuthLoginResponse, AuthRegisterResponse
from app.services.user_service import UserService
from app.managers.user_manager import UserManager
from app.auth.core.security import hash_password, create_access_token
from app.config.config import Messages

class AuthManager():

    @staticmethod
    async def register_user(db: AsyncSession, data: dict) -> AuthRegisterResponse:
        await UserManager.check_username(db, data["username"])
        await UserManager.check_email(db, data["email"])

        data["password"] = hash_password(data["password"])
        
        user = await UserService.create(db, data)
        await db.commit()

        token = create_access_token({"sub": user.email})
        return {
            "access_token": token,
            "token_type": "bearer",
            "user": user
        }

    @staticmethod
    async def login_user(db: AsyncSession, username_or_email: str, password: str) -> AuthLoginResponse:
        return await AuthService.authenticate(db, username_or_email, password)
