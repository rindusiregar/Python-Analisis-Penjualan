import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari CSV dengan separator ';'
df = pd.read_csv('penjualan.csv', sep=';')
print(df.columns)  # Untuk memeriksa nama kolom

#Melihat data frame
print(df.head())

# Total penjualan per jenis pelanggan
total_sales_per_customer_type = df.groupby('Customer_Type')['Sales'].sum().reset_index()

# Total penjualan per kota
total_sales_per_city = df.groupby('City')['Sales'].sum().reset_index()

# Total profit per kota
total_profit_per_city = df.groupby('City')['Profit'].sum().reset_index()

# Total profit per kota
total_profit_per_customer_type = df.groupby('Customer_Type')['Profit'].sum().reset_index()

# Mengatur gaya seaborn
sns.set(style="whitegrid")

# Grafik total penjualan per jenis pelanggan
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer_Type', y='Sales', data=total_sales_per_customer_type, palette='viridis')
plt.title('Total Sales per Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Total Sales')
plt.show()

# Grafik total penjualan per kota
plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Sales', data=total_sales_per_city, palette='viridis')
plt.title('Total Sales per City')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.show()

# Grafik total profit per kota
plt.figure(figsize=(6, 4))
sns.barplot(x='City', y='Profit', data=total_profit_per_city, palette='viridis')
plt.title('Total Profit per City')
plt.xlabel('City')
plt.ylabel('Total Profit')
plt.show()

# Visualisasi Profit per Jenis Pelanggan
plt.figure(figsize=(6, 4))
sns.barplot(x='Customer_Type', y='Profit', data=total_profit_per_customer_type, palette='viridis')
plt.title('Profit per Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Profit')
plt.show()
