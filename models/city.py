#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent the city class.

    Attributes:
        state_id (str): The state_id of the state.
        name (str):  Name of the city.
    """

    state_id = ""
    name = ""
