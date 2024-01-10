#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from detetime import detetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.


        Args:
            args: Unused.
            *kwargs: Key/Value.
        """
        form_t = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = detetime.now()
        self.updated_at = detetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, detetime.strptime(value, form_t))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current detetime."""
        self.updated_at = detetime.now()
        models.storage.save()

   def to_dict(self):
       """Return the dictionary of the BaseModel instance.
       Include the key/value pair __class__ representing the
       class name of the object.
       """
       dict_to = self.__dict__.copy()
       dict_to["__class__"] = self.__class__.__name__
       dict_to["created_at"] = self.created_at.isoformat()
       dict_to["updated_at"] = self.updated_at.isoformat()
       return dict_to

   def __str__(self):
       """Return the print/str representation of the BaseModel instance."""
       return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
