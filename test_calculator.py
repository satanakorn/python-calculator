import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:


    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(7, 0), 7)

    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 7), 4)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(7, 3), -4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_with_smaller_dividend(self):
        self.assertEqual(self.calc.divide(3, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_exact_division(self):
        self.assertEqual(self.calc.modulo(12, 4), 0)

    def test_modulo_with_smaller_dividend(self):
        self.assertEqual(self.calc.modulo(2, 5), 2)
        

if __name__ == '__main__':
    unittest.main()