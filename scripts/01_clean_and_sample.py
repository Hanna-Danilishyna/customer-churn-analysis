import pandas as pd

df = pd.read_csv("data/online_retail.csv")

# cleaning
df = df[df["Quantity"] > 0]
df = df[df["Price"] > 0]
df = df[df["Customer ID"].notna()]

# sample 300k
df_sample = df.sample(300000, random_state=42)

df_sample.to_csv("data/sample_data.csv", index=False)