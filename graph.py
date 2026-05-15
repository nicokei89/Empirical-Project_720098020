import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

analysis_df = pd.read_csv("../output/cleaned_happiness_income.csv")

# Graph 1: Line graph of average happiness by income group

# Define the correct order of income groups
# This makes the line go from low income to high income
income_order = [
    "Low income",
    "Lower middle income",
    "Upper middle income",
    "High income"
]

# Calculate the average happiness score for each income group
line_data = analysis_df.groupby("Income group")["Happiness Score"].mean()

# Reorder the income groups in a logical economic order
line_data = line_data.reindex(income_order)

# Set graph size
plt.figure(figsize=(9, 6))

# Create line graph with markers
plt.plot(
    line_data.index,
    line_data.values,
    marker="o"
)

# Add title and axis labels
plt.title("Graph 1:Average Happiness Score Across Income Groups")
plt.xlabel("World Bank Income Group")
plt.ylabel("Average Happiness Score")

# Rotate x-axis labels to make them easier to read
plt.xticks(rotation=30, ha="right")

# Add grid lines to make comparison easier
plt.grid(True, alpha=0.3)

# Improve layout
plt.tight_layout()

# Show graph
plt.show()

# Graph 2: Box plot of happiness score by income group

# Set graph size
plt.figure(figsize=(10, 6))

# Create box plot
sns.boxplot(
    data=analysis_df,
    x="Income group",
    y="Happiness Score"
)

# Add title and labels
plt.title("Graph 2 :Distribution of Happiness Scores by Income Group")
plt.xlabel("Income Group")
plt.ylabel("Happiness Score")

# Rotate x-axis labels
plt.xticks(rotation=45, ha="right")

# Improve layout
plt.tight_layout()

# Show graph
plt.show()

# Graph 3: Scatter plot coloured by income group

# Set graph size
plt.figure(figsize=(10, 6))

# Create scatter plot with different colours for each income group
sns.scatterplot(
    data=analysis_df,
    x="Economy",
    y="Happiness Score",
    hue="Income group",
    alpha=0.8
)

# Add title and labels
plt.title("Graph 3:Economy and Happiness Score by Income Group")
plt.xlabel("Economy")
plt.ylabel("Happiness Score")

# Move legend outside the plot
plt.legend(title="Income Group", bbox_to_anchor=(1.05, 1), loc="upper left")

# Improve layout
plt.tight_layout()

# Show graph
plt.show()

# Graph 4: Correlation heatmap

# Select numerical variables for correlation analysis
corr_vars = analysis_df[
    ["Happiness Score","Economy","Family","Health",
     "Freedom","Generosity","Corruption"]]

# Calculate correlation matrix
corr_matrix = corr_vars.corr()

# Set graph size
plt.figure(figsize=(9, 7))

# Create heatmap
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    center=0,
    fmt=".2f"
)

# Add title
plt.title("Graph 4:Correlation Between Happiness and Explanatory Factors")

# Improve layout
plt.tight_layout()

# Show graph
plt.show()

# Graph 5: Standardised regression coefficients


# Extract coefficients, excluding the constant
coefficients = standardised_model.params.drop("const")

# Create dataframe for plotting
coef_df = pd.DataFrame({
    "Variable": coefficients.index,
    "Coefficient": coefficients.values
})

# Sort by coefficient size
coef_df = coef_df.sort_values("Coefficient")

# Set graph size
plt.figure(figsize=(9, 6))

# Create horizontal bar chart
plt.barh(coef_df["Variable"], coef_df["Coefficient"])

# Add vertical line at zero
plt.axvline(0, linestyle="--")

# Add title and labels
plt.title("Graph 5:Standardised Regression Coefficients Explaining Happiness Score")
plt.xlabel("Standardised Coefficient")
plt.ylabel("Variable")

# Improve layout
plt.tight_layout()

# Show graph
plt.show()
