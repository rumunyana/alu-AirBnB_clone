#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestBase(unittest.TestCase):
    def test_initialization(self):
        amenity = Amenity()
        self.assertEqual(
            str(type(amenity)), "<class 'models.amenity.Amenity'>")
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
