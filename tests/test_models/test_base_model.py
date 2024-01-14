#!/usr/bin/python3
"""
Test suit for base_model module.
"""

import unittest
import json
import os
import time
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """Test cases for the `Base` class.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization_positive(self):
        """Test passing cases `BaseModel` initialization.
        """
        a = BaseModel()
        b_uuid = str(uuid.uuid4())
        b = BaseModel(id=b_uuid, name="The weeknd", album="Trilogy")
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(b.id, str)
        self.assertEqual(b_uuid, b.id)
        self.assertEqual(b.album, "Trilogy")
        self.assertEqual(b.name, "The weeknd")
        self.assertIsInstance(a.created_at, datetime)
        self.assertIsInstance(a.created_at, datetime)
        self.assertEqual(str(type(a)),
                         "<class 'models.base_model.BaseModel'>")

    def test_dict(self):
        """Test method for dict"""
        a = BaseModel()
        b_uuid = str(uuid.uuid4())
        b = BaseModel(id=b_uuid, name="The weeknd", album="Trilogy")
        b_dict = a.to_dict()
        self.assertIsInstance(b_dict, dict)
        self.assertIn('id', b_dict.keys())
        self.assertIn('created_at', b_dict.keys())
        self.assertIn('updated_at', b_dict.keys())
        self.assertEqual(b_dict['__class__'], type(b).__name__)
        with self.assertRaises(KeyError) as e:
            b.to_dict()

    def test_save(self):
        """Test method for save"""
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_save_storage(self):
        """Tests that storage.save() is called from save()."""
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_str(self):
        """Test method for str representation"""
        b = BaseModel()
        string = f"[{type(b).__name__}] ({b.id}) {b.__dict__}"
        self.assertEqual(b.__str__(), string)


if __name__ == "__main__":
    unittest.main()
