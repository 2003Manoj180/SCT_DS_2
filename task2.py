# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (if you downloaded Titanic CSV from Kaggle, put the correct path)
df = pd.read_csv("titanic.csv")

# ---------------------------
# 1. Basic Exploration
# ---------------------------
print(df.head())
print(df.info())
print(df.describe(include="all"))

# ---------------------------
# 2. Data Cleaning
# ---------------------------

# Check missing values
print("\nMissing values:\n", df.isnull().sum())

# Fill missing 'Age' with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing 'Embarked' with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

# Drop duplicates if any
df.drop_duplicates(inplace=True)

# ---------------------------
# 3. Exploratory Data Analysis
# ---------------------------

# Survival counts
sns.countplot(x='Survived', data=df)
plt.title("Survival Counts")
plt.show()

# Survival by gender
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title("Survival by Gender")
plt.show()

# Survival by class
sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title("Survival by Passenger Class")
plt.show()

# Age distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

# Survival vs Age
plt.figure(figsize=(8,5))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age vs Survival")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# ---------------------------
# 4. Insights & Patterns
# ---------------------------
# Example insights you can report:
# - Women had higher survival rates than men.
# - 1st class passengers survived more often than 3rd class.
# - Younger passengers (children) had higher survival chances.
# - Fare had a positive correlation with survival (richer passengers had higher chances).
