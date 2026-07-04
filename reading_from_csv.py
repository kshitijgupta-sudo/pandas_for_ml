#reading from csv file

import pandas as pd 
titanic = pd.read_csv('data/titanic.csv')


#head() method
print(titanic.head())
##specifc number of rows
print(titanic.head(10))

#tail() method
print(titanic.tail())
