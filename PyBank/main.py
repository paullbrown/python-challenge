
import pandas as pd
import os

budget_data_csv_path = "Resources/budget_data.csv"
budget_data_df = pd.read_csv(budget_data_csv_path, encoding="utf8")
budget_data_df.head()


total_months = budget_data_df["Months"].value_counts()
total_months


net_df = budget_data_df.sum("Profit/Losses", int)
net_df
