import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

# Load the cleaned dataset created by clean.py
clean_data_path = os.path.join("data", "clean_merged_analysis_data.csv")

# Create an output folder to save analysis results
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# Drop rows with missing values in the variables used for analysis
# This avoids errors in regression models and plots
analysis_df = merged_df.dropna(
    subset=["Happiness Score","Economy","Family","Health","Freedom","Generosity","Corruption","Income group"]).copy()

# Check final analysis dataset
analysis_df.shape

# Drop rows with missing values in the variables used for analysis
# This avoids errors in regression models and plots
analysis_df = merged_df.dropna(
    subset=["Happiness Score","Economy","Family","Health","Freedom","Generosity","Corruption","Income group"]).copy()

# Check final analysis dataset
analysis_df.shape

#  Regression model

# Define the dependent variable
# This is the outcome we want to explain
y = analysis_df["Happiness Score"]

# Define independent variables
# These are the factors that may explain happiness
X = analysis_df[
    ["Economy","Family","Health","Freedom","Generosity","Corruption" ]]

# Add a constant term to the regression model
# This is needed for statsmodels OLS regression
X = sm.add_constant(X)

# Run OLS regression
model = sm.OLS(y, X).fit()

# Print regression results
print(model.summary())

#  Regression model

# Define the dependent variable
# This is the outcome we want to explain
y = analysis_df["Happiness Score"]

# Define independent variables
# These are the factors that may explain happiness
X = analysis_df[
    ["Economy","Family","Health","Freedom","Generosity","Corruption" ]]

# Add a constant term to the regression model
# This is needed for statsmodels OLS regression
X = sm.add_constant(X)

# Run OLS regression
model = sm.OLS(y, X).fit()

# Print regression results
print(model.summary())

