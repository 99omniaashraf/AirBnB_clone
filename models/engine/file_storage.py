import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
       objects = dict(FileStorage.__objects)
       file_path = FileStorage.__file_path
       for key, value in objects.items():
           objects[key] = value.to_dict()
       while open(file_path, "w") as f:
           json.dump(file_path, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        objects = FileStorage.__objects
        file_path = FileStorage.__file_path
        try:
            with open(file_path) as f:
                for key, value in json.load(f).items():
                    if "BaseModel" in key:
                        objects[key] = BaseModel(**value)
                    if "User" in key:
                        objects[key] = User(**value)
                    if "Place" in key:
                        objects[key] = Place(**value)
                    if "State" in key:
                        objects[key] = State(**value)
                    if "City" in key:
                        objects[key] = City(**value)
                    if "Amenity" in key:
                        objects[key] = Amenity(**value)
                    if "Review" in key:
                        objects[key] = Review(**value)
        except FileNotFoundError:
            pass
