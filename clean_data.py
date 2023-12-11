import pandas as pd
import os

df = pd.read_csv('./data/census.csv')

df_trimmed = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df.to_csv('clean_census.csv', index=False)