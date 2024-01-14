#!/usr/bin/python3
"""
Unit tests for amenity module.
"""

import unittest
import os
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test cases for the class Amenity."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Tests method for class attributes"""

        a = Amenity()
        b = Amenity(**a.to_dict())
        abc = Amenity("hello", "wait", "in")

        k = f"{type(a).__name__}.{a.id}"
        self.assertIsInstance(a.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(abc.name, "")

    def test_init(self):
        """Test method for public instances"""
        a = Amenity()
        b = Amenity(**a.to_dict())
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.created_at, datetime)
        self.assertIsInstance(a.updated_at, datetime)
        self.assertEqual(a.updated_at, b.updated_at)

    def test_str(self):
        """Test method for str representation"""
        a = Amenity()
        string = f"[{type(a).__name__}] ({a.id}) {a.__dict__}"
        self.assertEqual(a.__str__(), string)

    def test_save(self):
        """Test method for save"""
        a = Amenity()
        old_update = a.updated_at
        a.save()
        self.assertNotEqual(a.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        a = Amenity()
        b = Amenity(**a.to_dict())
        a_dict = b.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(b).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()
