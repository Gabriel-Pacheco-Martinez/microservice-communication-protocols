from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True 