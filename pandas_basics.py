
# ==========================================
# MACHINE LEARNING JOURNEY
# Topic: Introduction to Pandas
# Author: Anjali
# ==========================================

# Importing Pandas library
import pandas as pd

# Creating a dataset using dictionary
data = {
    'Name': ['Aman', 'Riya', 'Rahul', 'Priya', 'Arjun'],
    'Age': [20, 21, 19, 22, 20],
    'Marks': [80, 90, 75, 95, 85]
}

# Converting dictionary into DataFrame
df = pd.DataFrame(data)

# Displaying complete dataset
print("STUDENT DATASET")
print(df)

# Displaying first five rows
print("\nFirst five rows:")
print(df.head())

# Displaying dataset information
print("\nDataset Information:")
print(df.info())

# Calculating average marks
print("\nAverage Marks:")
print(df['Marks'].mean())

# Finding maximum marks
print("\nMaximum Marks:")
print(df['Marks'].max())

# Finding minimum marks
print("\nMinimum Marks:")
print(df['Marks'].min())

# Displaying statistical summary
print("\nStatistical Summary:")
print(df.describe())
