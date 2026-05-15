# pandas is used for loading, cleaning, merging and analysing data
import pandas as pd

# numpy is used for numerical operations
import numpy as np

# matplotlib is used for creating graphs
import matplotlib.pyplot as plt

# seaborn is used to make statistical graphs more visually appealing
import seaborn as sns

# statsmodels is used for regression modelling
import statsmodels.api as sm

# Import packages for file paths and data loading
import os

# Downlaod the two dataset to desktop 
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Create file paths to the two data files stored on my Desktop
happiness_path = os.path.join(desktop, "World Happiness Report.csv")
income_path = os.path.join(desktop, "CLASS_2025_10_07.xlsx")

# Load the World Happiness Report dataset
happiness_df = pd.read_csv(happiness_path)

# Load the World Bank income group dataset from the correct Excel sheet
income_df = pd.read_excel(
    income_path,
    sheet_name="List of economies")

# Preview the first few rows of the happiness dataset
happiness_df.head()

# Display the first few rows of the happiness dataset
happiness_df.head()

# Display the first few rows of the World Bank income group dataset
income_df.head()

# Check the column names in the happiness dataset
print(happiness_df.columns)

# Check the column names in the World Bank dataset
print(income_df.columns)

# Check basic information about the happiness dataset
# This helps us see data types and missing values
happiness_df.info()

# Keep only the columns needed from the World Happiness Report
happiness_clean = happiness_df[
    ["Country","Happiness Score", "Economy", "Family","Health","Freedom",
     "Generosity","Corruption","Job Satisfaction","Region"]].copy()

# Keep only useful columns from the World Bank dataset
income_clean = income_df[
    ["Economy","Code", "Region","Income group"]].copy()

# Rename the World Bank region column so it does not conflict with the happiness region column
income_clean = income_clean.rename(
    columns={"Region": "World Bank Region"})

# Display cleaned happiness data
happiness_clean.head()

# Display cleaned World Bank income group data
income_clean.head()

# Some country names are written differently in the two datasets.
# For example, the happiness dataset may use "South Korea",
# while the World Bank dataset uses "Korea, Rep."
# This dictionary manually fixes common mismatches.

name_corrections = {
    "Czech Republic": "Czechia",
    "Slovakia": "Slovak Republic",
    "Russia": "Russian Federation",
    "South Korea": "Korea, Rep.",
    "North Korea": "Korea, Dem. People's Rep.",
    "Hong Kong S.A.R., China": "Hong Kong SAR, China",
    "Macedonia": "North Macedonia",
    "Kyrgyzstan": "Kyrgyz Republic",
    "Palestinian Territories": "West Bank and Gaza",
    "Egypt": "Egypt, Arab Rep.",
    "Iran": "Iran, Islamic Rep.",
    "Congo (Brazzaville)": "Congo, Rep.",
    "Congo (Kinshasa)": "Congo, Dem. Rep.",
    "Yemen": "Yemen, Rep.",
    "Syria": "Syrian Arab Republic",
    "Turkey": "Türkiye",
    "Somalia": "Somalia, Fed. Rep.",
    "Ivory Coast": "Côte d’Ivoire",
    "Venezuela": "Venezuela, RB"
}

# Create a new country column for merging
# This keeps the original country name unchanged
happiness_clean["Country_merge"] = happiness_clean["Country"].replace(name_corrections)

# Check the result
happiness_clean[["Country", "Country_merge"]].head()

# Merge the two datasets using the cleaned country names
merged_df = happiness_clean.merge(
    income_clean,
    left_on="Country_merge",
    right_on="Economy",
    how="left"
)

# Display the merged dataset
merged_df.head()

# Countries with missing income group did not match properly
unmatched = merged_df[merged_df["Income group"].isna()][["Country", "Country_merge"]]

# Display unmatched countries
unmatched

# Some economies may have missing income group in the World Bank file itself.
# We check how many countries are missing income group.
print("Number of countries without income group:", merged_df["Income group"].isna().sum())

# Count missing values in each column
merged_df.isna().sum()

# Rename columns after merging to make them clearer
merged_df = merged_df.rename(
    columns={
        "Economy_x": "Economy",
        "Economy_y": "World Bank Country"})

# Check column names again
print(merged_df.columns)

# Drop rows with missing values in the variables used for analysis
# This avoids errors in regression models and plots
analysis_df = merged_df.dropna(
    subset=["Happiness Score","Economy","Family","Health",
            "Freedom","Generosity","Corruption","Income group"]).copy()

# Check final analysis dataset
analysis_df.shape
