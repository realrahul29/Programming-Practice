import numpy as np

print("Enter elements for 5x3 matrix:")
matrix1 = []

for i in range(5):
    row = []
    for j in range(3):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix1.append(row)

print("\nEnter elements for 3x2 matrix:")
matrix2 = []

for i in range(3):
    row = []
    for j in range(2):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix2.append(row)

m1 = np.array(matrix1)
m2 = np.array(matrix2)

product = np.dot(m1, m2)

print("\n5x3 Matrix:")
print(m1)

print("\n3x2 Matrix:")
print(m2)

print("\nProduct Matrix (5x2):")
print(product)