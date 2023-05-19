#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
class TestBase(unittest.TestCase):
    def test_class_properties(self):
        # print(store["__file_path"], '====')
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(hasattr(FileStorage, "_FileStorage__file_path"), True)
        self.assertEqual(hasattr(FileStorage, "_FileStorage__objects"), True)
    
    def test_all(self):
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        base = BaseModel()
        key = key = "{}.{}".format(base.__class__.__name__, base.id)
        self.assertIn(key, storage.all().keys())

    def test_reload(self):
        self.assertIsInstance(storage.reload(), dict)

if __name__ == "__main__":
    unittest.main()