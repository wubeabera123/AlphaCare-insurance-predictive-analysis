# Data Summarization: Summary statistics and data types
def data_summary(df):
    # Summary statistics
    summary_stats = df.describe(include='all')
    print("Data Summary:\n", summary_stats)

    # Data types
    print("\nData Types:\n", df.dtypes)