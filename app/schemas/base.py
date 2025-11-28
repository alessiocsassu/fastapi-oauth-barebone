from pydantic import BaseModel

class BaseDelete(BaseModel):
    detail: str