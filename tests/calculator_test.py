import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, add(2, 3))
    
    
    # def test_add(self):
    #     expected = 5
    #     actual = add(2, 3)
    #     self.assertEqual(expected, actual)


    def test_subtract(self):
        self.assertEqual(3, subtract(10, 7))


    def test_divide(self):
        self.assertEqual(10, divide(30, 3))


    def test_multiply(self):
        self.assertEqual(27, multiply(3, 9))