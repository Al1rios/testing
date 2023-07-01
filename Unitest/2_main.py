
import unittest

class Test(unittest.TestCase):
    def test_sum_int(self):
        num1 = 10
        num2 = 20

        result = num1 + num2
        self.assertEqual(result, 30)

    def test_subtraction_int(self):
        num1 = 30
        num2 = -20

        self.assertEqual(30-20, 10)

if __name__ == '__main__':
    unittest.main()