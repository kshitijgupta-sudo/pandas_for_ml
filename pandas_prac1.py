import pandas as pd 

# Create a sample DataFrame

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})  

print(df)

#printing a specific column
print(df['Name'])

#each column is a series
#creating a series

ages = pd.Series([20, 25, 30, 35, 40], name='Age')
print(ages)

#some basic functions yk 
print(df["Age"].max())
print(ages.max())

#describe
print(df.describe())

