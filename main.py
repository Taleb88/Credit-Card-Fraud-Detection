import pandas as pd

df = pd.read_csv('creditcard.csv')

#print(df)

print(df.head())
print(df.tail())

sorted_column = df.sort_values(['Amount'], ascending=False)
top_20_amount = sorted_column.head(20)

top_20_amount.to_csv('top_20_amount.csv', index=False)