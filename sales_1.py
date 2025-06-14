import pandas as pd
import os

#download .csv file + parse date
path = os.path.join('CSV', 'sales.csv')
df = pd.read_csv(path, parse_dates=['order_date'])

#check order_date type
print()
print(df['order_date'].dtype)
print()

#df info
print(df.head())
print(f"\nRows: {df.shape[0]:}, columns: {df.shape[1]}")
print()
print(df.dtypes)

#add 'total' column
df['total'] = df['quantity'] * df['price']

#more df info
print(f"\nTotal volume: {sum(df['total']):.2f}")

print("Avg price by category:")
for cat, price in df.groupby('category')['price'].mean().items():
    print(f"{cat}: {price:.2f}")

print(f"Orders count after 2025-01-06: {(df['order_date'] > '2025-01-06').sum()}")

#save df to file
path = os.path.join('CSV', 'sales_cleaned_1.csv')
df.to_csv(path, index=False)