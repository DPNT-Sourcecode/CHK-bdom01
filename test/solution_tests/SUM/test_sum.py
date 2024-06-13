from lib.solutions.SUM import sum_solution
import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)
        
    def test_x_less_than_zero_raises_value_error(self):
        test_value = -1
        self.assertEqual(sum_solution.compute(test_value, 3),
                          ValueError(f"x={test_value} is not of type int"))



