# import all the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# import data
dataset = pd.read_csv("UberDataset.csv")


# Deleting null values
dataset.dropna(inplace=True)


# Removing Duplicates from dataset
dataset.drop_duplicates(inplace=True)


# Create a new figure
plt.figure(figsize=(10,5))


# Plot the graph
plt.subplot(1,2,2)
sns.countplot(dataset['PURPOSE'])
plt.xticks(rotation=90)


# Display the graph
plt.show()