import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # add(): 2 test cases
    def test_add_positive(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-5, 2), -3)

    # subtract(): 2 test cases
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    # multiply(): 2 test cases
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(3, -2), -6)

    # divide(): 2 test cases
    def test_divide_exact(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_divide_integer_result(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    # modulo(): 2 test cases
    def test_modulo_remainder(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_exact(self):
        self.assertEqual(self.calc.modulo(6, 3), 0)


if __name__ == '__main__':
    unittest.main()