from pydantic import BaseModel
from app.schemas.user import UserRead

class AuthRegisterResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserRead

class AuthLoginResponse(BaseModel):
    access_token: str
    token_type: str