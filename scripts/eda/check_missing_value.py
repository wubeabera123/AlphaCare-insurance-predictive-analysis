# Data Quality Assessment: Check for missing values
def check_missing_values(df):
    missing_values = df.isnull().sum()
    print("Missing Values per Column:\n", missing_values)