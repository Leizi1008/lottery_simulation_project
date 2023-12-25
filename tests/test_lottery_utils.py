import unittest
from lottery_utils import save_results_to_csv

class TestLotteryUtils(unittest.TestCase):
    def test_save_results_to_csv(self):
        # This is a simple test to ensure the function creates a file
        results = [([1, 2, 3, 4, 5, 6], [7])]
        save_results_to_csv(results, 'test_output.csv')
        with open('test_output.csv', 'r') as f:
            data = f.read()
        self.assertIn('1-2-3-4-5-6', data)

if __name__ == '__main__':
    unittest.main()
