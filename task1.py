# Load and Explore the Datatset
import pandas as pd
import numpy as np
# Load the dataset
df = pd.read_csv('Walmart_Sales.csv')
# Display the first few rows of the dataset
print(df.head())
# exploring the structure and info of the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())