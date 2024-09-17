import unittest
import pandas as pd
from scripts.eda.check_and_missing_value import handle_missing_values


class TestHandleMissingValues(unittest.TestCase):

    def setUp(self):
        """Set up a sample dataframe with missing values for testing."""
        data = {
            'Category': ['A', 'B', None, 'A', 'B', 'A', None],
            'Value': [10, 20, 30, None, 50, 60, None],
            'SkewedValue': [100, 200, 300, None, 1000, 5000, None]
        }
        self.df = pd.DataFrame(data)

    def test_handle_missing_values_categorical(self):
        """Test handling of missing values in categorical columns."""
        df_handled = handle_missing_values(self.df.copy())
        
        # Check that the missing values in 'Category' were replaced by the mode ('A')
        expected_category = ['A', 'B', 'A', 'A', 'B', 'A', 'A']
        self.assertListEqual(df_handled['Category'].tolist(), expected_category)

    def test_handle_missing_values_numerical_mean(self):
        """Test handling of missing values in numerical columns (mean for low skew)."""
        df_handled = handle_missing_values(self.df.copy())
        
        # Check that the missing value in 'Value' was replaced by the mean (mean is 34)
        expected_value = [10, 20, 30, 34, 50, 60, 34]
        self.assertListEqual(df_handled['Value'].tolist(), expected_value)

    def test_handle_missing_values_numerical_median(self):
        """Test handling of missing values in highly skewed numerical columns (median)."""
        df_handled = handle_missing_values(self.df.copy())
        
        # Check that the missing values in 'SkewedValue' were replaced by the median (median is 300)
        expected_skewed_value = [100, 200, 300, 300, 1000, 5000, 300]
        self.assertListEqual(df_handled['SkewedValue'].tolist(), expected_skewed_value)

    def test_no_missing_values(self):
        """Test that no changes are made to the dataframe if there are no missing values."""
        df_no_missing = self.df.dropna().copy()
        df_handled = handle_missing_values(df_no_missing)
        
        # The data should remain unchanged as there are no missing values
        pd.testing.assert_frame_equal(df_handled, df_no_missing)

if __name__ == '__main__':
    unittest.main()
