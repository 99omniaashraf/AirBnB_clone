#!/usr/bin/python3
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """class for State test."""
    def test_state(self):
        """Test."""
        state_instance = State()
        self.assertTrue(hasattr(state_instance, "id"))
        self.assertTrue(hasattr(state_instance, "created_at"))
        self.assertTrue(hasattr(state_instance, "updated_at"))
        self.assertTrue(hasattr(state_instance, "name"))
        self.assertIsInstance(state_instance.id, str)
        self.assertIsInstance(state_instance.created_at, datetime)
        self.assertIsInstance(state_instance.updated_at, datetime)
        self.assertIsInstance(state_instance.name, str)


if __name__ = "__main__":
    unittest.main()
