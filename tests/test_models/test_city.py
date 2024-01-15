#!/usr/bin/python3
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """class for City test."""
    def test_city(self):
        """Test."""
        city_instance = City()
        self.assertTrue(hasattr(city_instance, "id"))
        self.assertTrue(hasattr(city_instance, "created_at"))
        self.assertTrue(hasattr(city_instance, "updated_at"))
        self.assertTrue(hasattr(city_instance, "state_id"))
        self.assertTrue(hasattr(city_instance, "name"))
        self.assertIsInstance(city_instance.id, str)
        self.assertIsInstance(city_instance.created_at, datetime)
        self.assertIsInstance(city_instance.updated_at, datetime)
        self.assertIsInstance(city_instance.state_id, str)
        self.assertIsInstance(city_instance.name, str)


if __name__ = "__main__":
    unittest.main()
