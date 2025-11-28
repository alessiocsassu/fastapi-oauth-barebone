from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    BASE_URL: str
    
    model_config = ConfigDict(env_file=".env", extra="ignore")

settings = Settings()

class Messages():
    # GENERIC MESSAGES
    GENERIC_NOT_FOUND = "Resource not found"
    UPDATE_ERROR = "Error during update"
    DELETE_SUCCESS = "Deleted successfully"
    INVALID_TOKEN = "Invalid token"
    INVALID_OR_EXPIRED_TOKEN = "Invalid or expired token"
    
    # USER MESSAGES
    USER_NOT_FOUND = "User not found"
    ASSOCIED_USER_NOT_FOUND = "Associated user not found"
    INVALID_CREDENTIALS = "Email or password not valid"
    USERNAME_ALREADY_REGISTERED = "Username  already taken"
    EMAIL_ALREADY_REGISTERED = "Email already taken"
    USER_UPDATE_ERROR = "Error during user update"
    USER_DELETE_SUCCESS = "User deleted successfully"