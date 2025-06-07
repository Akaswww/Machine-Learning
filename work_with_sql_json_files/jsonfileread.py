# when u request data using API from any Website then those data which returns by your webiste is in json format mostly

import pandas as pd

df=pd.read_json('poem.json',lines=True)  #to read json fomrat file u need to add lines=true in your reading time
print(df.head())


