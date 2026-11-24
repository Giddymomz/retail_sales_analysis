# Retail Sales Analysis
# Gideon Momanyi | ALX Data Analytics Graduate
# Question: Which products, regions & months drive sales?

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('retail_sales.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()

print("Total Revenue:", df['Revenue'].sum())
print("\n--- Revenue by Product ---")
print(df.groupby('Product')['Revenue'].sum().sort_values(ascending=False))

print("\n--- Revenue by Region ---")
print(df.groupby('Region')['Revenue'].sum().sort_values(ascending=False))

print("\n--- Revenue by Month ---")
print(df.groupby('Month')['Revenue'].sum().sort_values(ascending=False))

# Chart 1: Revenue by Product
plt.figure()
df.groupby('Product')['Revenue'].sum().plot(kind='bar', title='Revenue by Product')
plt.ylabel('Revenue (KES)')
plt.tight_layout()
plt.savefig('revenue_by_product.png')
plt.show()

# Chart 2: Revenue by Region
plt.figure()
df.groupby('Region')['Revenue'].sum().plot(kind='bar', title='Revenue by Region', color='green')
plt.ylabel('Revenue (KES)')
plt.tight_layout()
plt.savefig('revenue_by_region.png')
plt.show()

# Chart 3: Revenue by Month
plt.figure()
df.groupby('Month')['Revenue'].sum().plot(kind='bar', title='Revenue by Month', color='orange')
plt.ylabel('Revenue (KES)')
plt.tight_layout()
plt.savefig('revenue_by_month.png')
plt.show()

print("\nInsight: Electronics in Nairobi in Dec drives highest sales. Stock up in Nov-Dec.")
