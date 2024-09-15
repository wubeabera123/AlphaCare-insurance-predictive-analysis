import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def detect_and_remove_outliers(df):
    # List of relevant columns for outlier detection
    relevant_columns = ['TotalPremium', 'TotalClaims']  # Add more relevant columns if needed
    
    # Loop through each relevant column
    for column in relevant_columns:
        # Calculate Q1 (25th percentile) and Q3 (75th percentile)
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        
        # Calculate Interquartile Range (IQR)
        IQR = Q3 - Q1
        
        # Define bounds for outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Detect outliers
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        
        # Remove outliers
        df = df[~((df[column] < lower_bound) | (df[column] > upper_bound))]
        
        # Visualize the column before and after removing outliers
        plt.figure(figsize=(12, 6))

        # Before removing outliers
        plt.subplot(1, 2, 1)
        sns.boxplot(x=outliers[column])
        plt.title(f'Boxplot of {column} (Outliers)')
        
        # After removing outliers
        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[column])
        plt.title(f'Boxplot of {column} (Cleaned)')
        
        plt.show()
    
    return df
