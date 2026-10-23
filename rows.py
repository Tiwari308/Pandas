import pandas as pd 

df = pd.read_json("sample_Data.json")

print('Display 10 rows of first')
print(df.head())

print('Display 10 rows of Last')
print(df.tail())

