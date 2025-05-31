import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sales.csv')

sales['quantity'] = pd.to_numeric(sales['quantity'], errors='coerce')
sales['price'] = pd.to_numeric(sales['price'], errors='coerce')

sales['total'] = sales['quantity'] * sales['price']

print(f"Total sales: {sales['total'].sum():.2f}")
print(f"Average sale: {sales['total'].mean():.2f}")
print(f"The most popular category: {sales['category'].mode()[0]}")

#без .copy(), потому что .groupby() не изменяет исходный df
mean_sales = sales.groupby('category')['total'].mean()
mean_sales.plot(kind='bar')
plt.ylabel('Average Sales')
plt.title('Average Sales by Category')
plt.show()

#без .copy(), потому что .groupby() не изменяет исходный df
daily_sales = sales.groupby('date')['total'].sum()
print(f"Max revenue date: {daily_sales.idxmax()}")

sales_sorted = sales.copy().sort_values('date')
sales_sorted.to_csv('sales_cleaned.csv', index=False)