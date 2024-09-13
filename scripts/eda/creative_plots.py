import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Visualization: Creative and informative plots
def Creative_Plots(df):
    # Total Premium by VehicleType
    plt.figure(figsize=(8, 6))
    sns.barplot(x='VehicleType', y='TotalPremium', data=df)  # Update with relevant columns
    plt.title('Total Premium by Vehicle Type')
    plt.xticks(rotation=45)
    plt.show()

    # Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[['TotalPremium', 'TotalClaims', 'SumInsured']].corr(), annot=True, cmap='coolwarm')  # Update with relevant columns
    plt.title('Correlation Heatmap')
    plt.show()

    # Total Claims by Citizenship
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Citizenship', y='TotalClaims', data=df)  # Update with relevant columns
    plt.title('Total Claims Distribution by Citizenship')
    plt.show()

