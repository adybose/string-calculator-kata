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

    def test_two_numbers_comma_separated(self):
        calc = StringCalculator()
        result = calc.add("1,5")
        self.assertEqual(result, 6)

    def test_multiple_numbers(self):
        calc = StringCalculator()
        result = calc.add("1,2,3,4")
        self.assertEqual(result, 10)

    def test_newlines_between_numbers(self):
        calc = StringCalculator()
        result = calc.add("1\n2,3")
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
