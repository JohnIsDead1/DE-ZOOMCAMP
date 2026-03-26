import pandas as pd
import sys


df = pd.DataFrame({"A": [1,2], "B": [3,4]})
print(df.head())

df.to_parquet(f"output_{sys.argv[1]}.parquet")