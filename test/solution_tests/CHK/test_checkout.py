from lib.solutions.CHK import checkout_solution
import unittest


class TestSum(unittest.TestCase):
    def test_basic(self):
        test_input = "ABCD"
        test_output = 115
        self.assertEqual(checkout_solution.checkout(test_input), test_output)
    
    def test_valid_input_with_offers(self):
        self.assertEqual(checkout_solution.checkout("AAABBBCCDD"), 130 + 45 + 30 + 40 + 30)
    
    def test_invalid_characters(self):
        self.assertEqual(checkout_solution.checkout("AAABBBCCDDX"), -1)
        
    def test_empty_string(self):
        self.assertEqual(checkout_solution.checkout(""), 0)
        
    def test_non_string_input(self):
        self.assertEqual(checkout_solution.checkout(123), -1)
        
    def test_no_offers(self):
        self.assertEqual(checkout_solution.checkout("ABCD"), 50 + 30 + 20 + 15)
        
    def test_only_offers(self):
        self.assertEqual(checkout_solution.checkout("AAAABB"), 130 + 50 + 45)