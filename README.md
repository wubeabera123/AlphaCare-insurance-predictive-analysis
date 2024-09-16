# Insurance Claims Analysis and Predictive Modeling

This project aims to perform a detailed analysis of insurance claims data. The analysis focuses on data quality checks, data cleaning, exploratory data analysis (EDA), A/B hypothesis testing, and predictive modeling to derive meaningful insights that can help in improving marketing strategies, attracting new clients, and optimizing insurance products.

## Project Structure

insurance-claims-analysis/ ├── data/ │ └── MachineLearningRating_v3.txt ├── notebooks/ │ ├── EDA.ipynb │ └── Hypothesis_Testing and Modeling.ipynb ├── src/ │ ├── data_quality_check.py │ ├── data_clean_processing.py │ ├── data_loader.py │ └── modeling.py └── tests/ ├── test_data_quality_check.py ├── test_data_clean_processing.py └── test_modeling.py └── README.md


## Installation

To run this project, you need to have Python installed. It is recommended to use a virtual environment to manage dependencies. 

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/insurance-claims-analysis.git
   cd insurance-claims-analysis

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
pip install dvc
dvc init
mkdir /path/to/your/local/storage
dvc remote add -d localstorage /path/to/your/local/storage
dvc add data/MachineLearningRating_v3.txt
git add data/MachineLearningRating_v3.txt.dvc .gitignore
git commit -m "Add data file to DVC"
dvc push


Data Quality Checks and Data Cleaning
Data Quality Checks
The DataQualityCheck class in src/data_quality_check.py performs basic data quality checks such as loading the data, displaying basic information, and checking for missing values.

Data Cleaning
The DataCleanProcessing class in src/data_clean_processing.py handles data cleaning by removing columns with more than 50% missing values and filling remaining missing values with appropriate statistics (mode for categorical and median for numerical).

Exploratory Data Analysis (EDA)
The EDA is performed in notebooks/EDA.ipynb, which includes:

Loading and cleaning the data
Generating a correlation matrix
Visualizing the correlation matrix with a heatmap
A/B Hypothesis Testing
The A/B hypothesis testing is detailed in notebooks/Hypothesis_Testing_and_Modeling.ipynb, including:

Data preparation and segmentation
Conducting chi-squared tests for categorical data
Conducting t-tests for numerical data
Interpreting the p-values and conducting power analysis
Hypotheses Tested:
No risk differences across provinces
No risk differences between zip codes
No significant margin differences between zip codes
No significant risk differences between women and men
Predictive Modeling
The predictive modeling is also detailed in notebooks/Hypothesis_Testing_and_Modeling.ipynb, which includes:

Data preparation and feature engineering
Encoding categorical data
Train-test split
Model building and evaluation for Linear Regression, Decision Trees, Random Forests, and XGBoost
Model evaluation using MAE, MSE, RMSE, and R² score
Feature importance analysis for Random Forest and XGBoost
Unit Tests
Unit tests for data quality checks, data cleaning, and modeling are provided in the tests directory. These tests ensure the robustness and correctness of the implemented methods.

To run the tests, use the following command:

pytest tests/
Continuous Integration
This project includes unit tests that can be integrated with CI/CD pipelines to ensure code quality and reliability.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Acknowledgments
Special thanks to the 10 Academy for the dataset and project inspiration.

### Documentation
Encouraging detailed documentation in the code and report writing is crucial. Ensure that all classes and methods have appropriate docstrings, and use comments to explain non-trivial code sections.

### Conclusion
By integrating DVC for data version control, performing thorough data quality checks and cleaning, conducting exploratory data analysis, executing A/B hypothesis testing, and building robust predictive models, this project provides a comprehensive approach to understanding and leveraging insurance claims data for strategic business decisions.
