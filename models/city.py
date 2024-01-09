#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    Attributes:
        state_id: The state id.
        name: The name of the city.
    """

    state_id = ""
    name = ""
