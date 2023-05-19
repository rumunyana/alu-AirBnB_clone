#!/usr/bin/python3
import unittest
from models.user import User


class TestBase(unittest.TestCase):
    def test_initialization(self):
        user = User()
        self.assertEqual(
            str(type(user)), "<class 'models.user.User'>")
        self.assertEqual(str(type(user.id)), "<class 'str'>")
        self.assertEqual(
            str(type(user.created_at)), "<class 'datetime.datetime'>")
        self.assertEqual(
            str(type(user.updated_at)), "<class 'datetime.datetime'>")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
