import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# a) Total profit line plot
plt.plot(df["Month"], df["Total Profit"])
plt.title("Total Profit")
plt.show()

# b) Multiline plot
plt.plot(df["Month"], df["Product1"], label="Product1")
plt.plot(df["Month"], df["Product2"], label="Product2")
plt.legend()
plt.show()

# c) Bar chart
plt.bar(df["Month"], df["Facecream"])
plt.bar(df["Month"], df["Facewash"])
plt.show()

# d) Pie chart
total_sales = df.sum()
plt.pie(total_sales[1:], labels=total_sales.index[1:], autopct='%1.1f%%')
plt.show()