from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import UserCreate
from app.auth.schemas.auth_schema import AuthRegisterResponse, AuthLoginResponse
from app.auth.managers.auth_manager import AuthManager

router = APIRouter(prefix="", tags=["Auth"])

@router.post("/register", response_model=AuthRegisterResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await AuthManager.register_user(db, user.dict())

@router.post("/login", response_model=AuthLoginResponse, status_code=status.HTTP_200_OK)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    return await AuthManager.login_user(db, form_data.username, form_data.password)