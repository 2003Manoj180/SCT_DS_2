import pandas as pd

# Load the dataset
df = pd.read_csv('train.csv')

# Check for missing values
print(df.isnull().sum())

# Fill missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Drop Cabin column (too many missing values)
df.drop('Cabin', axis=1, inplace=True)

# Drop rows with missing Embarked
df.dropna(subset=['Embarked'], inplace=True)



