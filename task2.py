import pandas as pd

files = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]

dataframes = [pd.read_csv(file) for file in files]
df = pd.concat(dataframes, ignore_index=True)
df = df[df["product"] == "pink morsel"]
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)
df["sales"] = df["price"] * df["quantity"]
output_df = df[["sales", "date", "region"]]
output_df.to_csv("pink_morsel_sales.csv", index=False)
print("pink_morsel_sales.csv has been created successfully.")