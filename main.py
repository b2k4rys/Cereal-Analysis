# ALL THE NEEDED LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


try:
    df = pd.read_csv('cereal.csv')
except FileNotFoundError:
    exit()


# BASIC COMMANDS 
print("First 5 rows of the dataset:\n")
print(df.head())

print("Dataset Information:\n")
df.info()

print("\nDescriptive Statistics:")
print(df.describe())