from fastapi.params import Query

from database import SessionLocal


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def common_parameters(
    page_num: int = Query(default=1, description="Page Number"),
    page_size: int = Query(default=10, description="Page Size"),
    search: str = Query(default=None, description="Search parameter")
):
    return {"page_num": page_num, "page_size": page_size, "search": search}
