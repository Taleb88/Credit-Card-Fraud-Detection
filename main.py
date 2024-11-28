import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('creditcard.csv')

#print(df)
#print(df.head())
#print(df.tail())

sorted_column = df.sort_values(['Amount'], ascending=False)
top_20_amount = sorted_column.head(20)

top_20_amount = top_20_amount.rename({'Time': 'Entry'}, axis='columns')

top_20_amount.to_csv('top_20_amount.csv', index=False)

# creating a pie chart based on top 20 amount
#x_axis = top_20_amount['Amount']
#y_axis = top_20_amount['Amount']