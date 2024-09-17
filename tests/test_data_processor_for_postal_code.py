import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from scipy.stats import ttest_ind
from scripts.data_processor_for_postal_code import  DataProcessor, Tester, ReportGenerator


class TestDataProcessor(unittest.TestCase):
    
    def setUp(self):
        """Set up some sample data for testing."""
        data = {
            'PostalCode': [1050, 2050, 3050, 4050, 5050],
            'Value': [10, 20, 30, 40, 50]
        }
        self.df = pd.DataFrame(data)
        self.processor = DataProcessor(self.df)

    def test_segment_data(self):
        """Test data segmentation based on given conditions."""
        conditions = {
            'GroupA': self.df['PostalCode'] < 3000,
            'GroupB': self.df['PostalCode'] >= 3000
        }
        segments = self.processor.segment_data('PostalCode', conditions)

        expected_group_a = self.df[self.df['PostalCode'] < 3000]
        expected_group_b = self.df[self.df['PostalCode'] >= 3000]
        
        assert_frame_equal(segments['GroupA'], expected_group_a)
        assert_frame_equal(segments['GroupB'], expected_group_b)

    def test_segment_data_empty_group(self):
        """Test that a segmentation with no matching data results in an empty group warning."""
        conditions = {
            'EmptyGroup': self.df['PostalCode'] > 10000  # No data matches this condition
        }
        segments = self.processor.segment_data('PostalCode', conditions)
        
        self.assertEqual(segments, {})  # No valid groups should be returned


class TestTester(unittest.TestCase):
    
    def setUp(self):
        """Set up two groups for T-test."""
        data = {
            'Value': [10, 15, 10, 20, 25]
        }
        self.group1 = pd.DataFrame(data)
        self.group2 = pd.DataFrame({'Value': [30, 35, 40, 45, 50]})
        self.tester = Tester()

    def test_t_test(self):
        """Test the t-test for comparing two groups."""
        p_value = self.tester.t_test(self.group1, self.group2, 'Value')
        self.assertIsInstance(p_value, float)
        self.assertGreaterEqual(p_value, 0)

    def test_analyze_results_significant(self):
        """Test analyze_results when the p-value is below the threshold (significant)."""
        result = self.tester.analyze_results(0.03)
        self.assertEqual(result, 'Significant difference')

    def test_analyze_results_not_significant(self):
        """Test analyze_results when the p-value is above the threshold (not significant)."""
        result = self.tester.analyze_results(0.07)
        self.assertEqual(result, 'No significant difference')

    def test_add_result(self):
        """Test adding a result to the results dictionary."""
        self.tester.add_result('T-test for Value', 0.03, 'Significant difference')
        expected_result = {
            'description': 'T-test for Value',
            'p_value': 0.03,
            'result': 'Significant difference'
        }
        self.assertDictEqual(self.tester.results, expected_result)


class TestReportGenerator(unittest.TestCase):

    def test_generate_report(self):
        """Test report generation from the results."""
        results = {
            'description': 'T-test for Value',
            'p_value': 0.03,
            'result': 'Significant difference'
        }
        report_generator = ReportGenerator(results)
        report = report_generator.generate_report()
        
        expected_report = (
            "Description: T-test for Value\n"
            "P-value: 0.03\n"
            "Analysis Result: Significant difference\n"
        )
        
        self.assertEqual(report, expected_report)


if __name__ == '__main__':
    unittest.main()
