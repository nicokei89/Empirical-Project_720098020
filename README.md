# To what extent is happiness explained by economic strength compared with social, health, and governance factors across different World Bank income groups?
## Motivation 
I choose this topic becasue hapiness is something which surround us through out our life and was related to evryone, but it is hard to explain it in just one word happy and it is hard to define if in just one factor. In economics, countries are often compared using income, GDP, or economic development. This creates the impression that richer countries should automatically be happier. However, in real life, happiness is also affected by social support, health, personal freedom, trust and the quality of institutions. A country may be economically strong, but people may still feel unhappy if they face stress, poor social relationships, limited freedom or low trust in society.
This makes the topic interesting because it allows me to question whether money is really the main driver of happiness. By using the World Happiness Report, I can examine different factors that may contribute to national happiness, such as Economy, Family, Health, Freedom, Generosity and Corruption. By combining this with World Bank income groups, I can also compare whether happiness patterns differ between low-income, middle-income and high-income countries.
The motivation of this project is therefore to move beyond a simple “richer means happier” explanation. Instead, the project aims to explore whether economic strength remains important when social, health and governance-related factors are also considered. This makes the topic suitable for a data-driven blog because it connects economic development with wider human well-being.
## Libraries and Packages Used

This project uses Python and several libraries for data cleaning, analysis, modelling, and visualisation.

- **os**  
  Used to manage file paths and help Python locate the datasets stored in the project folder.

- **pandas**  
  Used to load, clean, merge, and organise the datasets. It is the main library used for handling the World Happiness Report data and the World Bank income classification data.

- **numpy**  
  Used for numerical operations and data handling during the analysis process.

- **matplotlib**  
  Used to create basic visualisations and customise graphs.

- **seaborn**  
  Used to create clearer and more visually appealing statistical graphs, such as scatter plots, box plots, and bar charts.

- **statsmodels**  
  Used to run regression models and examine the relationship between happiness scores and explanatory variables such as GDP per capita, social support, health, freedom, and corruption.

- **scikit-learn**  
  Used for standardising variables with `StandardScaler`, which helps compare variables measured on different scales.
## Variables Used

The main dependent variable in this project is:

- **Happiness Score**  
  This measures the overall happiness or life satisfaction level of each country. It is the main outcome variable used in the analysis.

The main explanatory variables are:

- **Economy**  
  Represents GDP per capita. It is used to measure the economic strength of each country.

- **Family**  
  Represents social support. It is used to measure whether people have support from family, friends, or society.

- **Health**  
  Represents healthy life expectancy. It is used to measure the health condition and expected healthy lifespan of people in each country.

- **Freedom**  
  Measures the freedom people feel they have to make life choices.

- **Generosity**  
  Measures generosity within society, such as donations or helping behaviour.

- **Corruption**  
  Measures perceptions of corruption in government and business.

- **Income Group**  
  Taken from the World Bank income classification dataset. It is used to compare happiness and related factors across different income groups, such as high-income, upper-middle-income, lower-middle-income, and low-income economies.

## Procedure

- Open this GitHub repository.

- Download all files from the repository.

- Keep all files in the same project folder. Do not rename any files.

- Open **Anaconda Navigator**.

- Launch **Jupyter Notebook** from Anaconda Navigator.

- In Jupyter Notebook, open the downloaded project folder.

- Open `blog.ipynb`.

- Run the notebook cells from top to bottom.

- The notebook contains the full project, including:
  - data loading
  - data cleaning
  - data merging
  - data analysis
  - regression modelling
  - graph creation
  - final blog writing

-Then you will get all the 5 graph and two table 

- If running the separate Python files, run them in this order:
  1. `clean.py`
  2. `analysis.py`
  3. `graph.py`
  4. `blog.ipynb`

- The cleaned datasets and graphs are also included in the repository, so the final blog can be read directly from `blog.ipynb`.

- All required data files are included in this repository, so the project should run directly from the downloaded folder.

## Important Note

Please keep the original file names unchanged, as the notebook and Python scripts use these file names to load the datasets and generate the outputs.

