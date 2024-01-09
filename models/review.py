#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.
    Attributes:
        place_id: The place id.
        user_id: The user id.
        text: The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
