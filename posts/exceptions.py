from fastapi import status

from exceptions import CustomHTTPException


class PostNotFound(CustomHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Post not found with given id"

