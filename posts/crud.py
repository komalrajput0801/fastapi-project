from typing import List, Union, Dict, Any

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from crud_base import CRUDBase
from posts.exceptions import PostNotFound
from posts.models import Post
from posts.schemas import PostCreate


class CRUDPost(CRUDBase[Post, PostCreate, PostCreate]):
    def create(self, db: Session, *, obj_in: PostCreate) -> Post:
        try:
            post_obj = super().create(db, obj_in=obj_in)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user id")
        return post_obj

    def get_multi(self, db: Session, page_size: int = 10, page_num: int = 1) -> List[Post]:
        return super().get_multi(db, offset=(page_num - 1) * page_size, limit=page_size)

    def get_posts_of_user(
        self, db: Session, user_id: int, skip: int = 0, limit: int = 10
    ) -> List[Post]:
        return db.query(Post).filter(Post.user_id == user_id).offset(skip).limit(limit).all()

    def update(self, db: Session, post_id: int, obj_in: Union[PostCreate, Dict[str, Any]]) -> Post:
        db_post = super().get(db, post_id)
        if not db_post:
            raise PostNotFound()
        return super().update(db, db_obj=db_post, obj_in=obj_in)


post = CRUDPost(Post)
