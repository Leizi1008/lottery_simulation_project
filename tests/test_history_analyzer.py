import unittest
from history_analyzer import analyze_history

class TestHistoryAnalyzer(unittest.TestCase):
    def test_analyze_history(self):
        # This is a simple test to check if the function returns a dictionary
        stats = analyze_history('historical_lottery_data.csv')
        self.assertIsInstance(stats, dict)

if __name__ == '__main__':
    unittest.main()
