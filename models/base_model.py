#!/usr/bin/python3
""" Defines the BaseModel class """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel

            Args:
                - *args : unused
                - **kwargs : key/value
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update the public instance attribute updated_at"""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Return a representation of a BaseModel instance in a string"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
