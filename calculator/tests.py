import unittest
from pkg.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.evaluate("1 + 2"), 3)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate("5 - 3"), 2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate("2 * 4"), 8)

    def test_division(self):
        self.assertEqual(self.calculator.evaluate("10 / 2"), 5)

    def test_complex_expression(self):
        self.assertEqual(self.calculator.evaluate("10 + 2 * 3 - 6 / 2"), 13)

    def test_invalid_token(self):
        with self.assertRaisesRegex(ValueError, "invalid token: a"):
            self.calculator.evaluate("1 + a")

    def test_invalid_expression(self):
        with self.assertRaisesRegex(ValueError, "not enough operands for operator +"):
            self.calculator.evaluate("1 +")

    def test_empty_expression(self):
        self.assertIsNone(self.calculator.evaluate(""))

    def test_whitespace_expression(self):
        self.assertIsNone(self.calculator.evaluate("   "))
        
    def test_division_by_zero(self):
        with self.assertRaisesRegex(ZeroDivisionError, "float division by zero"):
            self.calculator.evaluate("1 / 0")

if __name__ == '__main__':
    unittest.main()
