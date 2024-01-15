#!/usr/bin/python3
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class for Amenity test."""
    def test_amenity(self):
        """Test."""
        amenity_instance = State()
        self.assertTrue(hasattr(amenity_instance, "id"))
        self.assertTrue(hasattr(amenity_instance, "created_at"))
        self.assertTrue(hasattr(amenity_instance, "updated_at"))
        self.assertTrue(hasattr(amenity_instance, "name"))
        self.assertIsInstance(amenity_instance.id, str)
        self.assertIsInstance(amenity_instance.created_at, datetime)
        self.assertIsInstance(amenity_instance.updated_at, datetime)
        self.assertIsInstance(amenity_instance.name, str)


if __name__ = "__main__":
    unittest.main()
