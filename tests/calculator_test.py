import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, add(2, 3))
    pass