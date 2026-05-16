1. Load the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("labels.csv")

# Display first 5 rows
df.head()
________________________________________

2. Number of Rows and Columns
print("Dataset Shape:", df.shape)
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

3. Type of Input Features
print(df.dtypes)
Feature Description


4. Target Variable Description
The target variable in this dataset is:
target = "class"
The dataset contains the following defect categories:
print(df["class"].unique())
Classes Present
•	normal 
•	scratch 
•	dent 
•	stain 


5. Missing Value Check
print(df.isnull().sum())
Output
Column	Missing Values
filename	0
class	0
