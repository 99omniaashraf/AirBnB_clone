#!/usr/bin/python3
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """class for Place test."""
    def test_place(self):
        """Test."""
        place_instance = Place()
        self.assertTrue(hasattr(place_instance, "id"))
        self.assertTrue(hasattr(place_instance, "created_at"))
        self.assertTrue(hasattr(place_instance, "updated_at"))
        self.assertTrue(hasattr(place_instance, "city_id"))
        self.assertTrue(hasattr(place_instance, "user_id"))
        self.assertTrue(hasattr(place_instance, "name"))
        self.assertTrue(hasattr(place_instance, "description"))
        self.assertTrue(hasattr(place_instance, "number_rooms"))
        self.assertTrue(hasattr(place_instance, "number_bathrooms"))
        self.assertTrue(hasattr(place_instance, "max_guest"))
        self.assertTrue(hasattr(place_instance, "price_by_night"))
        self.assertTrue(hasattr(place_instance, "latitude"))
        self.assertTrue(hasattr(place_instance, "longtude"))
        self.assertTrue(hasattr(place_instance, "amenity_ids"))
        self.assertIsInstance(place_instance.id, str)
        self.assertIsInstance(place_instance.created_at, datetime)
        self.assertIsInstance(place_instance.updated_at, datetime)
        self.assertIsInstance(place_instance.city_id, str)
        self.assertIsInstance(place_instance.user_id, str)
        self.assertIsInstance(place_instance.name, str)
        self.assertIsInstance(place_instance.description, str)
        self.assertIsInstance(place_instance.number_rooms, int)
        self.assertIsInstance(place_instance.number_bathrooms, int)
        self.assertIsInstance(place_instance.max_guest, int)
        self.assertIsInstance(place_instance.price_by_night, int)
        self.assertIsInstance(place_instance.latitude, float)
        self.assertIsInstance(place_instance.longtude, float)
        self.assertIsInstance(place_instance.amenity_ids, list)


if __name__ = "__main__":
    unittest.main()
