import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        calc = StringCalculator()
        result = calc.add("")
        self.assertEqual(result, 0)
    
    def test_single_number_returns_itself(self):
        calc = StringCalculator()
        result = calc.add("1")
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
