import pandas as pd

df = pd.read_csv("books.csv")

print(df)  # all books

author = input("Enter author: ")
print(df[df["author"] == author])

publisher = input("Enter publisher: ")
print(df[df["publisher"] == publisher])

print("Cheapest:", df.loc[df["price"].idxmin()])
print("Costliest:", df.loc[df["price"].idxmax()])

print(df.sort_values("year"))