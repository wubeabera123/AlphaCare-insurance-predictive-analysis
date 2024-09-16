import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind, f_oneway


class DataProcessor:
    """Responsible for preparing and segmenting the data."""

    def __init__(self, data):
        self.data = data

    def select_kpi(self, kpi_col):
        """Select the KPI for the A/B test (e.g., TotalClaims, TotalPremium)."""
        if kpi_col not in self.data.columns:
            raise ValueError(
                f"KPI column '{kpi_col}' does not exist in the dataset.")
        return self.data[kpi_col]

    def segment_data(self, feature, group_conditions):
        """
        Segments the data into multiple groups based on the conditions provided.
        """
        groups = {}
        for group_name, condition in group_conditions.items():
            group = self.data[condition]
            if group.empty:
                raise ValueError(
                    f"Segmentation resulted in an empty group for '{group_name}'")
            groups[group_name] = group
        return groups


class HypothesisTester:
    """Handles hypothesis testing using statistical methods."""

    def __init__(self):
        self.results = []

    def chi_squared_test(self, group_a, group_b, feature):
        """Performs a chi-squared test for categorical features."""
        contingency_table = pd.crosstab(group_a[feature], group_b[feature])
        chi2, p_value, _, _ = chi2_contingency(contingency_table)
        return p_value

    def t_test(self, group_a, group_b, kpi):
        """Performs a t-test for numerical features like claims or premium."""
        stat, p_value = ttest_ind(group_a[kpi], group_b[kpi], equal_var=False)
        return p_value

    def anova_test(self, groups, kpi):
        """Performs an ANOVA test for comparing multiple groups."""
        kpi_values = [group[kpi] for group in groups.values()]
        f_stat, p_value = f_oneway(*kpi_values)
        return p_value

    def analyze_results(self, p_value, alpha=0.05):
        """Analyzes the p-value to accept or reject the null hypothesis."""
        if p_value < alpha:
            return "Reject the null hypothesis"
        return "Fail to reject the null hypothesis"

    def add_result(self, hypothesis_name, p_value, result):
        """Stores the test results."""
        self.results.append({
            'Hypothesis': hypothesis_name,
            'P-Value': p_value,
            'Result': result
        })


class ReportGenerator:
    """Generates a report from the hypothesis test results."""

    def __init__(self, results):
        self.results = results

    def generate_report(self):
        """Compiles the results into a report format."""
        report = "\nA/B Hypothesis Testing Report\n"
        report += "="*40 + "\n"

        for result in self.results:
            report += f"Hypothesis: {result['Hypothesis']}\n"
            report += f"P-Value: {result['P-Value']}\n"
            report += f"Result: {result['Result']}\n"
            report += "-"*40 + "\n"

        return report
