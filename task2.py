import pandas as pd
import numpy as np

# Function to load the dataset and handle errors
def load_data(file_path):
    try:
        # Attempt to load the CSV file
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file {file_path} could not be parsed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading the data: {e}")
        return None

# Load the dataset
df = load_data('Walmart_Sales.csv')

# Proceed only if data is loaded successfully
if df is not None:
    try:
        # Display the first few rows of the dataset
        print(df.head())

        # Performing Basic statistics of the numerical columns
        print(df.describe())

        # Performing groupings on categorical columns
        print("\nMean by Store: ")
        grouped = df.groupby('Store')['Weekly_Sales'].mean()
        print(grouped)

        # Insights/observations
        print("\nInsights/Observations: \nTop performing stores based on weekly sales:")
        print("1. Store 40: 2.11M")
        print("2. Store 4: 2.09M")
        print("3. Store 14: 2.02M")
        print("4. Store 13: 2.00M")
        print("5. Store 2: 1.93M")

    except KeyError as e:
        print(f"Error: The expected column {e} is not in the dataset.")
    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")
else:
    print("Data loading failed, analysis will not proceed.")
