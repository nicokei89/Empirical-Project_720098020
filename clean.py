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

# Import StandardScaler for standardised regression
from sklearn.preprocessing import StandardScaler

# Create file paths for the two datasets stored on Desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

happiness_path = os.path.join(desktop, "WHR25_Data_Figure_2.1v3.xlsx")
income_path = os.path.join(desktop, "CLASS_2025_10_07.xlsx")

# Load the World Happiness Report 2025 data file
# The latest available observations in this file are from 2024
happiness_df = pd.read_excel(
    happiness_path,
    sheet_name="Data for Figure 2.1 (2011–2024)"
)

# Keep only the latest available year in the happiness dataset
happiness_df = happiness_df[happiness_df["Year"] == 2024].copy()

# Load the World Bank income classification dataset
income_df = pd.read_excel(
    income_path,
    sheet_name="List of economies"
)

# Preview the happiness dataset
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

# Select only the happiness variables needed for this project
happiness_clean = happiness_df[
    ["Country name","Life evaluation (3-year average)","Explained by: Log GDP per capita",
     "Explained by: Social support","Explained by: Healthy life expectancy",
     "Explained by: Freedom to make life choices", "Explained by: Generosity", 
     "Explained by: Perceptions of corruption"]].copy()

# Rename long column names into shorter names for easier analysis
happiness_clean = happiness_clean.rename(
    columns={"Country name": "Country", "Life evaluation (3-year average)": "Happiness Score",
             "Explained by: Log GDP per capita": "Economy","Explained by: Social support": "Family",
             "Explained by: Healthy life expectancy": "Health","Explained by: Freedom to make life choices": "Freedom",
             "Explained by: Generosity": "Generosity","Explained by: Perceptions of corruption": "Corruption"})

# Select only the income classification variables needed for this project
income_clean = income_df[["Economy","Code","Region","Income group"]].copy()

# Rename the World Bank region column to make it clearer after merging
income_clean = income_clean.rename(
    columns={"Region": "World Bank Region"})

# Preview the cleaned happiness dataset
happiness_clean.head()

# Display cleaned World Bank income group data
income_clean.head()
# Some country names are written differently in the two datasets
# This dictionary corrects those differences before merging
name_corrections = {
    "Czechia": "Czechia",
    "Czech Republic": "Czechia",
    "Slovakia": "Slovak Republic",
    "Russia": "Russian Federation",
    "South Korea": "Korea, Rep.",
    "North Korea": "Korea, Dem. People's Rep.",
    "Hong Kong S.A.R. of China": "Hong Kong SAR, China",
    "Hong Kong S.A.R., China": "Hong Kong SAR, China",
    "Macedonia": "North Macedonia",
    "Kyrgyzstan": "Kyrgyz Republic",
    "State of Palestine": "West Bank and Gaza",
    "Palestinian Territories": "West Bank and Gaza",
    "Egypt": "Egypt, Arab Rep.",
    "Iran": "Iran, Islamic Rep.",
    "Congo (Brazzaville)": "Congo, Rep.",
    "Congo (Kinshasa)": "Congo, Dem. Rep.",
    "Yemen": "Yemen, Rep.",
    "Syria": "Syrian Arab Republic",
    "Turkey": "Türkiye",
    "Türkiye": "Türkiye",
    "Somalia": "Somalia, Fed. Rep.",
    "Ivory Coast": "Côte d’Ivoire",
    "Venezuela": "Venezuela, RB",
    "Gambia": "Gambia, The",
    "Laos": "Lao PDR"
}

# Create a new country column for merging with the World Bank dataset
happiness_clean["Country_merge"] = happiness_clean["Country"].replace(name_corrections)

# Check the original and corrected country names
happiness_clean[["Country", "Country_merge"]].head()

# Merge the happiness dataset with the World Bank income group dataset
# The merge is based on corrected country names
merged_df = happiness_clean.merge(
    income_clean,
    left_on="Country_merge",
    right_on="Economy",
    how="left",
    suffixes=("_happiness", "_worldbank")
)

# Preview the merged dataset
merged_df.head()

# Rename columns after merging to avoid confusion
# Economy_happiness means GDP contribution from the happiness dataset
# Economy_worldbank means country/economy name from the World Bank dataset
merged_df = merged_df.rename(
    columns={
        "Economy_happiness": "Economy",
        "Economy_worldbank": "World Bank Country"
    }
)

# Check the new column names
print(merged_df.columns)

# Find countries that did not match with the World Bank income dataset
unmatched = merged_df[merged_df["Income group"].isna()][
    ["Country", "Country_merge"]
]

# Display unmatched countries
unmatched

# Count how many countries do not have an income group after merging
print("Number of countries without income group:", merged_df["Income group"].isna().sum())

# Count missing values in each column of the merged dataset
merged_df.isna().sum()

# Drop rows with missing values in the variables used for analysis
# This avoids errors in regression models and plots
analysis_df = merged_df.dropna(
    subset=["Happiness Score","Economy","Family","Health",
            "Freedom","Generosity","Corruption","Income group"]).copy()

# Check final analysis dataset
analysis_df.shape
