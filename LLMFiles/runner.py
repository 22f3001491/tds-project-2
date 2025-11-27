import pandas as pd

df = pd.read_csv("demo-audio-data.csv", header=None)
cutoff = 31494

# Assuming the numbers are in the first column (index 0)
filtered_sum = df[df[0] > cutoff][0].sum()

print(int(filtered_sum))
