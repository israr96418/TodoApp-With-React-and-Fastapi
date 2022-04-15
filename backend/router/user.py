from typing import List

from fastapi import APIRouter, status, Depends, HTTPException,Response
from sqlalchemy.orm import Session

from .. import database, schema, models

router = APIRouter(
    # prefix="/user",
    tags=["user"]
)


# Get all User
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schema.OutSchema])
def get_user(db: Session = Depends(database.get_db)):
    all_user = db.query(models.User).all()
    return all_user


# Get single user
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.OutSchema)
def get_user(id: int, db: Session = Depends(database.get_db)):
    single_user = db.query(models.User).filter(models.User.id == id).first()
    if single_user:
        return single_user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Your post with {id} is not found")


# Create User
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.OutSchema)
def create_user(user: schema.InSchema, db: Session = Depends(database.get_db)):
    User_data = models.User(**user.dict())
    db.add(User_data)
    db.commit()
    db.refresh(User_data)
    return User_data


# Update User
@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schema.OutSchema)
def create_user(id: int, user: schema.UpDateSchema, db: Session = Depends(database.get_db)):
    user_data = db.query(models.User).filter(models.User.id == id)
    data = user_data.first()
    print("data: ", data.name)
    if data:
        user_data.update(user.dict(), synchronize_session=False)
        db.commit()
        return user_data.first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Your post with {id} is not found")


# Delete User
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def create_user(id: int, db: Session = Depends(database.get_db)):
    user_data = db.query(models.User).filter(models.User.id == id)
    data = user_data.first()
    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Your post with {id} is not found")
    else:
        user_data.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
