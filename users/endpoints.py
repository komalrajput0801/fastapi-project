from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Query
from fastapi.security import OAuth2PasswordRequestForm
from pydantic.types import List
from sqlalchemy.orm import Session

from dependencies import get_db, common_parameters
from users.schemas import UserCreate, User, UserBase
from users.crud import user
from users.utils import verify_password, create_access_token

router = APIRouter(prefix="/users")


@router.get("/", response_model=List[User])
def get_users(session: Session = Depends(get_db), common_params: dict = Depends(common_parameters)):
    return user.get_multi(
        session,
        page_num=common_params["page_num"],
        page_size=common_params["page_size"],
        search=common_params["search"],
    )


@router.post("/register", response_model=User)
def register_user(user_schema: UserCreate, session: Session = Depends(get_db)):
    return user.create(session, user_schema)


@router.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: int, session: Session = Depends(get_db)):
    return user.get(session, user_id)


@router.put("/{user_id}", response_model=User)
def edit_user(user_id: int, update_data: UserBase, session: Session = Depends(get_db)):
    return user.update(session, user_id, update_data)


@router.delete("/{user_id}")
def remove_user(user_id: int, session: Session = Depends(get_db)):
    user.remove(session, id=user_id)
    return {"message": "User Deleted successfully"}


@router.post("/login/")
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    user_in_db = user.get_user_by_username(session, form_data.username)
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username"
        )
    if not verify_password(form_data.password, user_in_db.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    return {"access_token": create_access_token(user_in_db.username), "token_type": "Bearer"}
