import sys
import os
import unittest
from src.calculator import fun1, fun2, fun3, fun4, fun5, fun6, fun7

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 25)  # (2+3)*5 = 25
        self.assertEqual(calculator.fun4(1, 2, 3), 9)   # (1+2)*3 = 9
        self.assertEqual(calculator.fun4(5, 5, 2), 20)  # (5+5)*2 = 20
    
    def test_fun5(self):
        self.assertEqual(fun5(10, 2), 5.0)
        self.assertEqual(fun5(20, 4), 5.0)
        self.assertEqual(fun5(9, 3), 3.0)

    def test_fun5_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            fun5(10, 0)

    def test_fun6(self):
        self.assertEqual(fun6(2, 3), 8)
        self.assertEqual(fun6(5, 2), 25)
        self.assertEqual(fun6(10, 0), 1)

    def test_fun7(self):
        self.assertEqual(fun7([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(fun7([10, 20, 30]), 20.0)
        self.assertEqual(fun7([5]), 5.0)

    def test_fun7_empty_list(self):
        with self.assertRaises(ValueError):
            fun7([])

   

if __name__ == '__main__':
    unittest.main()