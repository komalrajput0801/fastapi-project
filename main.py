from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from database import Base, engine, SessionLocal
from users.endpoints import router as user_router
from posts.endpoints import api_router as post_router
from users.models import Project

app = FastAPI()

# The create_all() function uses the engine object to create all the defined table objects and stores the information in
# metadata.
# Metadata is used to tie together the database structure so it can be quickly accessed inside SQLAlchemy.
# It’s often useful to think of metadata as a kind of catalog of Table objects with optional information about the engine
# and the connection
# Base.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(post_router)

session = SessionLocal()
project1 = Project("test4", 1)
project2 = Project("test5", 1)
session.add(project1)
session.add(project2)


# If you're not raising an HTTPException then normally any other uncaught exception(suppose value error from validator)
# will generate a 500 response (an Internal Server Error). If your intent is to respond with some other custom error message
# and HTTP status when raising a particular exception - say, ValueError - then you can use add a global exception handler
# to your app
# @app.exception_handler(ValueError)
# async def value_error_exception_handler(request: Request, exc: ValueError):
#     return JSONResponse(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         content={"message": str(exc)},
#     )
