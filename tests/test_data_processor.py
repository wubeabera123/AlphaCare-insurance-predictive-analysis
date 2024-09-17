import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from scipy.stats import chi2_contingency, ttest_ind, f_oneway
from scripts.data_processor import DataProcessor, HypothesisTester, ReportGenerator  # Assuming these are in a file named data_processor.py

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        """Prepare some sample data."""
        data = {
            'FeatureA': ['A', 'A', 'B', 'B', 'A'],
            'FeatureB': ['X', 'Y', 'X', 'Y', 'X'],
            'KPI': [100, 150, 200, 250, 300]
        }
        self.df = pd.DataFrame(data)

    def test_select_kpi_success(self):
        """Test that KPI column selection works as expected."""
        processor = DataProcessor(self.df)
        kpi = processor.select_kpi('KPI')
        pd.testing.assert_series_equal(kpi, self.df['KPI'])

    def test_select_kpi_nonexistent_column(self):
        """Test that selecting a non-existent KPI column raises an error."""
        processor = DataProcessor(self.df)
        with self.assertRaises(ValueError) as context:
            processor.select_kpi('NonExistentKPI')
        self.assertEqual(
            str(context.exception),
            "KPI column 'NonExistentKPI' does not exist in the dataset."
        )

    def test_segment_data_success(self):
        """Test data segmentation based on conditions."""
        processor = DataProcessor(self.df)
        conditions = {
            'GroupA': self.df['FeatureA'] == 'A',
            'GroupB': self.df['FeatureB'] == 'X'
        }
        groups = processor.segment_data('FeatureA', conditions)
        expected_group_a = self.df[self.df['FeatureA'] == 'A']
        expected_group_b = self.df[self.df['FeatureB'] == 'X']
        assert_frame_equal(groups['GroupA'], expected_group_a)
        assert_frame_equal(groups['GroupB'], expected_group_b)

    def test_segment_data_empty_group(self):
        """Test that segmenting data resulting in an empty group raises an error."""
        processor = DataProcessor(self.df)
        conditions = {
            'EmptyGroup': self.df['FeatureA'] == 'Z'
        }
        with self.assertRaises(ValueError) as context:
            processor.segment_data('FeatureA', conditions)
        self.assertEqual(
            str(context.exception),
            "Segmentation resulted in an empty group for 'EmptyGroup'"
        )


class TestHypothesisTester(unittest.TestCase):

    def setUp(self):
        """Prepare test data."""
        data_a = {'Feature': ['X', 'Y', 'X'], 'KPI': [10, 20, 30]}
        data_b = {'Feature': ['Y', 'Y', 'X'], 'KPI': [15, 25, 35]}
        self.group_a = pd.DataFrame(data_a)
        self.group_b = pd.DataFrame(data_b)
        self.tester = HypothesisTester()

    def test_chi_squared_test(self):
        """Test chi-squared test for categorical features."""
        p_value = self.tester.chi_squared_test(self.group_a, self.group_b, 'Feature')
        self.assertIsInstance(p_value, float)
        self.assertGreaterEqual(p_value, 0)

    def test_t_test(self):
        """Test t-test for numerical features."""
        p_value = self.tester.t_test(self.group_a, self.group_b, 'KPI')
        self.assertIsInstance(p_value, float)
        self.assertGreaterEqual(p_value, 0)

    def test_anova_test(self):
        """Test ANOVA for comparing multiple groups."""
        groups = {
            'GroupA': self.group_a,
            'GroupB': self.group_b
        }
        p_value = self.tester.anova_test(groups, 'KPI')
        self.assertIsInstance(p_value, float)
        self.assertGreaterEqual(p_value, 0)

    def test_analyze_results(self):
        """Test analyze_results for p-value interpretation."""
        result = self.tester.analyze_results(0.03)  # p-value less than alpha
        self.assertEqual(result, "Reject the null hypothesis")
        
        result = self.tester.analyze_results(0.06)  # p-value greater than alpha
        self.assertEqual(result, "Fail to reject the null hypothesis")

    def test_add_result(self):
        """Test adding a result to the results list."""
        self.tester.add_result("Hypothesis 1", 0.01, "Reject the null hypothesis")
        self.assertEqual(len(self.tester.results), 1)
        self.assertEqual(self.tester.results[0]['Hypothesis'], "Hypothesis 1")
        self.assertEqual(self.tester.results[0]['P-Value'], 0.01)
        self.assertEqual(self.tester.results[0]['Result'], "Reject the null hypothesis")


class TestReportGenerator(unittest.TestCase):

    def test_generate_report(self):
        """Test report generation from hypothesis test results."""
        results = [
            {'Hypothesis': "Hypothesis 1", 'P-Value': 0.01, 'Result': "Reject the null hypothesis"},
            {'Hypothesis': "Hypothesis 2", 'P-Value': 0.06, 'Result': "Fail to reject the null hypothesis"}
        ]
        generator = ReportGenerator(results)
        report = generator.generate_report()
        expected_report = (
            "\nA/B Hypothesis Testing Report\n"
            "========================================\n"
            "Hypothesis: Hypothesis 1\n"
            "P-Value: 0.01\n"
            "Result: Reject the null hypothesis\n"
            "----------------------------------------\n"
            "Hypothesis: Hypothesis 2\n"
            "P-Value: 0.06\n"
            "Result: Fail to reject the null hypothesis\n"
            "----------------------------------------\n"
        )
        self.assertEqual(report, expected_report)


if __name__ == "__main__":
    unittest.main()
