from lib.solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        
    def test_x_less_than_zero_raises_value_error(self):
        test_value = -1
        assert sum_solution.compute(test_value, 3) == ValueError(f"x={test_value} is not of type int")


