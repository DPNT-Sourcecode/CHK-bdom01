from lib.solutions.CHK import checkout_solution
import unittest


# class TestSum(unittest.TestCase):
#     def test_basic(self):
#         test_input = "ABCDE"
#         test_output = 115
#         self.assertEqual(checkout_solution.checkout(test_input), test_output)
        
#     def test_none_input(self):
#         self.assertEqual(checkout_solution.checkout(None), -1)
        
class TestCheckoutFunction(unittest.TestCase):
    # 130, 40, 30, 40, 45 = 285
    def test_valid_input_with_offers(self):
        self.assertEqual(checkout_solution.checkout("AAABBBCCDDEE"), 130 + 40 + 30 + 40 + 30)
    
    def test_invalid_characters(self):
        self.assertEqual(checkout_solution.checkout("AAABBBCCDDX"), -1)
        
    def test_empty_string(self):
        self.assertEqual(checkout_solution.checkout(""), 0)
        
    def test_non_string_input(self):
        self.assertEqual(checkout_solution.checkout(123), -1)
        
    def test_A_offers(self):
        self.assertEqual(checkout_solution.checkout("AAAAA"), 200)
        self.assertEqual(checkout_solution.checkout("AAAAAA"), 200 + 50)
        self.assertEqual(checkout_solution.checkout("AAAAAAA"), 200 + 100)
        
    def test_B_E_offers(self):
        self.assertEqual(checkout_solution.checkout("EEB"), 80)  # E's offer gives a free B
        self.assertEqual(checkout_solution.checkout("EEEEBB"), 160)
        
    def test_no_offers(self):
        self.assertEqual(checkout_solution.checkout("ABCD"), 50 + 30 + 20 + 15)
        
    def test_complex_case(self):
        self.assertEqual(checkout_solution.checkout("AAAAABBBCCDEE"), 200 + 50 + 45 + 30 + 20*2 + 15 + 80)


