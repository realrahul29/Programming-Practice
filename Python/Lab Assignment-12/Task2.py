import pandas as pd

df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive
print(df[df["Department"] == "Automotive"])

# b) Employee details by ID
emp_id = int(input("Enter Employee ID: "))
print(df[df["Employee ID"] == emp_id])

# c) All Developers
print(df[df["Designation"] == "Developer"])