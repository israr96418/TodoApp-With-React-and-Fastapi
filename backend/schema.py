from pydantic import BaseModel


class InSchema(BaseModel):
    # id:int
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class OutSchema(BaseModel):
    id:int
    name: str
    email: str
    password:str

    class Config:
        orm_mode = True


class UpDateSchema(BaseModel):
    name: str
    email: str
    password:str

    class Config:
        orm_mode = True
