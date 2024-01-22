#!/usr/bin/python3
"""Define a user class"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """Represent a BaseModel class user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
