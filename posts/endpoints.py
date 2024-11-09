from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db, common_parameters
from posts.crud import post
from posts.schemas import PostSchema, PostCreate
from users.models import User
from users.utils import get_current_user

api_router = APIRouter()


@api_router.post("/posts", response_model=PostSchema)
def create_new_post(post_schema: PostCreate, session: Session = Depends(get_db)):
    return post.create(session, obj_in=post_schema)


@api_router.get("/posts", response_model=List[PostSchema])
def get_posts(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_db),
    common_params: dict = Depends(common_parameters),
):
    return post.get_multi(
        session, page_num=common_params["page_num"], page_size=common_params["page_size"]
    )


@api_router.get("/posts/{post_id}", response_model=PostSchema)
def get_post_by_id(post_id: int, session: Session = Depends(get_db)):
    return post.get(session, post_id)


@api_router.get("/posts/user/{user_id}", response_model=List[PostSchema])
def get_user_posts(user_id: int, session: Session = Depends(get_db)):
    return post.get_posts_of_user(session, user_id)


@api_router.put("/posts/{post_id}", response_model=PostSchema)
def edit_post(post_id: int, update_data: PostCreate, session: Session = Depends(get_db)):
    return post.update(session, post_id=post_id, obj_in=update_data)


@api_router.delete("/posts/{post_id}")
def remove_post(post_id: int, session: Session = Depends(get_db)):
    post.remove(session, id=post_id)
    return {"message": "Post Deleted successfully"}
