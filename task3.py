import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        # Data Visualization for the average weekly sales per store
        grouped = df.groupby('Store')['Weekly_Sales'].mean()
        
        # Bar chart
        grouped.plot(kind='bar', figsize=(12, 6))
        plt.title('Bar graph for Average Weekly Sales per Store')
        plt.xlabel('Store')
        plt.ylabel('Average Weekly Sales')
        plt.tight_layout()
        plt.show()

        # Line Chart of average weekly sales per store
        grouped.plot(kind='line', figsize=(12, 6))
        plt.title('Line graph for Average Weekly Sales per Store')
        plt.xlabel('Store')
        plt.ylabel('Average Weekly Sales')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Histogram of the average weekly sales per store
        grouped.plot(kind='hist', figsize=(12, 6), bins=20)
        plt.hist(grouped, bins=20, color='skyblue', edgecolor='black')
        plt.title('Histogram of Average Weekly Sales per Store')
        plt.xlabel('Average Weekly Sales')
        plt.ylabel('Number of Stores')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

        # Scatter plot of the average weekly sales per store
        plt.figure(figsize=(12, 6))
        plt.scatter(grouped.index, grouped.values, color='lightblue', edgecolor='black')
        plt.title('Scatter plot of Average Weekly Sales per Store')
        plt.xlabel('Store')
        plt.ylabel('Average Weekly Sales')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except KeyError as e:
        print(f"Error: The expected column {e} is not in the dataset.")
    except Exception as e:
        print(f"An unexpected error occurred during plotting: {e}")
else:
    print("Data loading failed, visualization will not proceed.")
