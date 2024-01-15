#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.file_storage = FileStorage()

    def testDown(self):
        """
        """
        if os.path.exists(self.file_storage.__file_path):
            os.remove(self.file_storage.__file_path)

    def test_all(self):
        """
        """
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, self.file_storage.FileStorage__objects)

    def test_new(self):
        """
        """
        obj = BaseModel()
        self.file_storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.od}"
        self.assertIn(key, self.file_storage.FileStorage__objects)
        self.assertEqual(self.file_storage.FileStorage__objects[key], obj)

    def test_save_and_reload(self):
        """
        """
        obj1 = BaseModel()
        obj2 = User()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        self.file_storage.save()
        new_file_storage = FileStorage()
        new_file_storage.reload()
        self.assertEqual(new_file_storage.all(), self.file_storage.all())

    def test_reload_empty_file(self):
        """
        """
        with open(self.file_storage.__file_path, 'w', encoding='utf-8') as file:
            file.write('')
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})

    def test_reload_nonexistent_file(self):
        """
        """
        self.file_storage.__file_path = 'nonexistent_file.json'
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})


if __name__ == '__main__':
    unittest.main()
