#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    def test_initialization(self):
        model = BaseModel()
        self.assertEqual(
            str(type(model)), "<class 'models.base_model.BaseModel'>")
        self.assertEqual(str(type(model.id)), "<class 'str'>")
        self.assertEqual(
            str(type(model.created_at)), "<class 'datetime.datetime'>")
        self.assertEqual(
            str(type(model.updated_at)), "<class 'datetime.datetime'>")

    def test_string(self):
        model = BaseModel()
        dt = "[{}] ({}) {}".format(
            model.__class__.__name__, model.id, model.__dict__)
        self.assertEqual(str(model), dt)

    def test_save(self):
        model = BaseModel()
        time = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, time)

    def test_dict(self):
        model = BaseModel()
        obj = model.to_dict()
        self.assertEqual(obj["id"], model.id)
        self.assertEqual(obj["__class__"], model.__class__.__name__)
        self.assertEqual(obj["created_at"], model.created_at.isoformat())
        self.assertEqual(obj["updated_at"], model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
