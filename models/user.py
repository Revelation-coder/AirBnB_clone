#!/usr/bin/python3
"""Class User a child of  BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Our class User with user attributtes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
