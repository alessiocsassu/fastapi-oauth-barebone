from fastapi import FastAPI
from app.auth.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router

app = FastAPI(title="Backend API")

app.include_router(auth_router)
app.include_router(users_router)
