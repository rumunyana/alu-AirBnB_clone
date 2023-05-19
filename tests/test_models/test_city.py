#!/usr/bin/python3
import unittest
from models.city import City


class TestBase(unittest.TestCase):
    def test_initialization(self):
        city = City()
        self.assertEqual(
            str(type(city)), "<class 'models.city.City'>")
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")


if __name__ == "__main__":
    unittest.main()
