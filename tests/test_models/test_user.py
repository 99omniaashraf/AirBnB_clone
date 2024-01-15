#!/usr/bin/python3
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.Testcase):
    """class for User test."""
    def test_user(self):
        """Test."""
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "id"))
        self.assertTrue(hasattr(user_instance, "created_at"))
        self.assertTrue(hasattr(user_instance, "updated_at"))
        self.assertTrue(hasattr(user_instance, "email"))
        self.assertTrue(hasattr(user_instance, "password"))
        self.assertTrue(hasattr(user_instance, "first_name"))
        self.assertTrue(hasattr(user_instance, "last_name"))
        self.assertIsInstance(user_instance.id, str)
        self.assertIsInstance(user_instance.created_at, datetime)
        self.assertIsInstance(user_instance.updated_at, datetime)
        self.assertIsInstance(user_instance.email, str)
        self.assertIsInstance(user_instance.password, str)
        self.assertIsInstance(user_instance.first_name, str)
        self.assertIsInstance(user_instance.last_name, str)


if __name__ = "__main__":
    unittest.main()
