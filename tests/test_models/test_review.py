#!/usr/bin/python3
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """class for Review test."""
    def test_review(self):
        """Test."""
        review_instance = Review()
        self.assertTrue(hasattr(review_instance, "id"))
        self.assertTrue(hasattr(review_instance, "created_at"))
        self.assertTrue(hasattr(review_instance, "updated_at"))
        self.assertTrue(hasattr(review_instance, "place_id"))
        self.assertTrue(hasattr(review_instance, "user_id"))
        self.assertTrue(hasattr(review_instance, "text"))
        self.assertIsInstance(review_instance.id, str)
        self.assertIsInstance(review_instance.created_at, datetime)
        self.assertIsInstance(review_instance.updated_at, datetime)
        self.assertIsInstance(review_instance.place_id, str)
        self.assertIsInstance(review_instance.user_id, str)
        self.assertIsInstance(review_instance.text, str)


if __name__ = "__main__":
    unittest.main()
