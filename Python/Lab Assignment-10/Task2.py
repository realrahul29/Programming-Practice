import pandas as pd

data = {
    "State": ["A", "B", "C", "D", "E"],
    "Area": [100, 200, 150, 300, 250],
    "Population": [1000, 5000, 3000, 7000, 6000]
}

df = pd.DataFrame(data)

print(df)

print("Largest Area:", df.loc[df["Area"].idxmax()])
print("Largest Population:", df.loc[df["Population"].idxmax()])

df["Density"] = df["Population"] / df["Area"]

print("Highest Density:", df.loc[df["Density"].idxmax()])