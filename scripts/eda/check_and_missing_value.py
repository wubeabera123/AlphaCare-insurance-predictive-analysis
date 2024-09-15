def handle_missing_values(df):
    # Step 1: Check for missing values
    missing_values = df.isnull().sum()
    print("Missing Values per Column:\n", missing_values)

    # Step 2: Handle missing values
    for column in df.columns:
        if df[column].isnull().sum() > 0:  # If the column has missing values
            if df[column].dtype == 'object':  # Categorical columns
                # Fill categorical missing values with mode or a placeholder
                df[column].fillna(df[column].mode()[0], inplace=True)
                print(f"Missing values in '{column}' handled by mode.")
            else:  # Numerical columns
                # Fill numerical missing values with mean or median
                if df[column].skew() < 1:  # Low skewness, use mean
                    df[column].fillna(df[column].mean(), inplace=True)
                    print(f"Missing values in '{column}' handled by mean.")
                else:  # High skewness, use median
                    df[column].fillna(df[column].median(), inplace=True)
                    print(f"Missing values in '{column}' handled by median.")
    
    print("All missing values handled.")
    return df