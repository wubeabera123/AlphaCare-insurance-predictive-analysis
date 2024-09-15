import matplotlib.pyplot as plt
import seaborn as sns

# Univariate Analysis: Numerical and Categorical features
def Univariate_Analysis(df):
    # Numerical columns to plot histograms for
    numerical_cols = ['TotalPremium', 'TotalClaims', 'SumInsured', 'NumberOfDoors']  # Update with relevant columns
    for col in numerical_cols:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

    # Categorical columns to plot bar charts for
    categorical_cols = ['CoverType', 'Citizenship', 'Bank', 'VehicleType']  # Update with relevant columns
    for col in categorical_cols:
        plt.figure(figsize=(8, 6))
        sns.countplot(y=df[col], order=df[col].value_counts().index)
        plt.title(f'Distribution of {col}')
        plt.show()