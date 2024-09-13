import matplotlib.pyplot as plt
import seaborn as sns

# Bivariate/Multivariate Analysis: Correlation and relationships
def Bivariate_Analysis(df):
    # Correlation matrix for numerical features
    correlation = df[['TotalPremium', 'TotalClaims']].corr()  # Update with relevant columns
    print("Correlation Matrix:\n", correlation)

    # Scatter plot for relationships between TotalPremium and TotalClaims
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='TotalPremium', y='TotalClaims', data=df)
    plt.title('TotalPremium vs TotalClaims')
    plt.show()

