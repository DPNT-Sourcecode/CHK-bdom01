from lib.solutions.CHK import checkout_solution
import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        test_input = "ABCD"
        test_output = 115
        self.assertEqual(checkout_solution.checkout(test_input), test_output)
    