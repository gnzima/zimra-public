import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from zimra import tax_calculator


class TestFiscalizationFunctions(unittest.TestCase):

    def test_tax_calculator(self):
        # Test cases for the tax calculator
        test_cases = [
            (100.00, 15, 13.04),  # Normal scenario with 15% tax
            (200.00, 20, 33.33),  # 20% tax rate
            (0, 15, 0),           # Zero sale amount
            (100.00, 0, 0),       # Zero tax rate
        ]

        for sale_amount, tax_rate, expected in test_cases:
            with self.subTest(sale_amount=sale_amount, tax_rate=tax_rate, expected=expected):
                self.assertAlmostEqual(tax_calculator(sale_amount, tax_rate), expected, places=2)



if __name__ == '__main__':
    unittest.main()
