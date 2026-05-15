import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

analysis_df = pd.read_csv("../output/cleaned_happiness_income.csv")

# Summary statistics help us understand the scale and spread of each variable
analysis_df[["Happiness Score","Economy","Family","Health",
             "Freedom","Generosity","Corruption"]].describe()

#  Regression model

# Define the dependent variable
# This is the outcome we want to explain
y = analysis_df["Happiness Score"]

# Define independent variables
# These are the factors that may explain happiness
X = analysis_df[
    ["Economy","Family","Health","Freedom","Generosity","Corruption"]]

# Add a constant term to the regression model
# This is needed for statsmodels OLS regression
X = sm.add_constant(X)

# Run OLS regression
model = sm.OLS(y, X).fit()

# Print regression results
print(model.summary())

# Standardised regression coefficient plot

# Import StandardScaler
from sklearn.preprocessing import StandardScaler

# Define dependent variable
y = analysis_df["Happiness Score"]

# Define explanatory variables
X = analysis_df[
    ["Economy","Family","Health","Freedom", "Generosity","Corruption"]]

# Standardise the explanatory variables
# This puts all variables on the same scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert the scaled data back into a dataframe
X_scaled = pd.DataFrame(
    X_scaled,
    columns=X.columns,
    index=X.index
)

# Add a constant term for the regression
X_scaled = sm.add_constant(X_scaled)

# Run OLS regression using standardised variables
standardised_model = sm.OLS(y, X_scaled).fit()

# Print regression results
print(standardised_model.summary())
