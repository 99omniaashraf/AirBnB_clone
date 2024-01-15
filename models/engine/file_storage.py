#!/usr/bin/python3
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """class meant to manage JSON file.


    Attributes:
        __file_path: default path to save JSON serializations to file
        __objects: dict of items with BaseModel.
    """
    __file_path = 'HBnB_objects.json'
    __objects = dict()

    def __init__(self):
        pass

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets a new object aas value in __objects with key
        '<object class name>.<object.id>'


        Args:
            obj: BaseModel object to be added to __objects.
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        json_dict = dict()
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_dict))

    def reload(self):
        """Deserializes the JSON file at __file_path into __objects."""
        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        class_dict = dict()
        for c in classes:
            class_dict[c.__name__] = c
        if path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if content is not None and content != '':
                    json_dict = json.loads(content)
                    for key, value in json_dict.items():
                        obj_class = class_dict[value['__class__']]
                        self.__objects[key] = obj_class(**value)
        else:
            pass
