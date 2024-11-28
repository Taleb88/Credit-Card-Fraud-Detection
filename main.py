import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('creditcard.csv')

#print(df)
#print(df.head())
#print(df.tail())

sorted_column = df.sort_values(['Amount'], ascending=False)
top_20_amount = sorted_column.head(20)

top_20_amount = top_20_amount.rename({'Time': 'Case'}, axis='columns')

top_20_amount.to_csv('top_20_amount.csv', index=False)

# creating a pie chart via matplotlib
top_20_case_data = top_20_amount['Case']
top_20_amount_data = top_20_amount['Amount']

plt.pie(top_20_amount_data, labels=top_20_amount_data)

plt.title('Amounts per Case')

plt.show()