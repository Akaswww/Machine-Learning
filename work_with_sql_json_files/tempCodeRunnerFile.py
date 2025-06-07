import pandas as pd

df=pd.read_json('test.json',lines=True)  #to read json fomrat file u need to add lines=true in your reading time
print(df.head())
