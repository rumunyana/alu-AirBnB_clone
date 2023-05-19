#!/usr/bin/python3
import unittest
from models.state import State


class TestBase(unittest.TestCase):
    def test_initialization(self):
        state = State()
        self.assertEqual(
            str(type(state)), "<class 'models.state.State'>")
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
