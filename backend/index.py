from fastapi import FastAPI
from backend.router import user
from fastapi.middleware.cors import CORSMiddleware
from backend import models,database
# this used to convert all the sqlalchemy model into tables
# it means this will create tables for u
models.Base.metadata.create_all(bind=database.engine)

# but when u used alembic(lightweight database migration tools) noo need of this
# if client want to change/delete some field in the database without alembic it is not possible


app = FastAPI()

origin=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user.router)