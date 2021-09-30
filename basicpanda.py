import pandas as pd
mat = pd.read_csv('sample.csv')
#print(type(mat))
print(mat.info())
print(mat.describe())