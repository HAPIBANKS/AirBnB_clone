#!/usr/bin/python3
"""
test suit for the city module.
"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from datetime import datetime

ch = City()
c2 = City(**ch.to_dict())
c3 = City("hello", "wait", "in")


class TestCity(unittest.TestCase):
    """Test cases for the `City` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""
        k = f"{type(ch).__name__}.{ch.id}"
        self.assertIsInstance(ch.name, str)
        self.assertEqual(c3.name, "")
        ch.name = "Abuja"
        self.assertEqual(ch.name, "Abuja")

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(ch.id, str)
        self.assertIsInstance(ch.created_at, datetime)
        self.assertIsInstance(ch.updated_at, datetime)
        self.assertEqual(ch.updated_at, c2.updated_at)

    def test_save(self):
        """Test method for save"""
        old_update = ch.updated_at
        ch.save()
        self.assertNotEqual(ch.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        a_dict = c2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(c2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(ch, c2)


if __name__ == "__main__":
    unittest.main()
