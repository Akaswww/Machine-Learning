import pandas as pd

url = "https://raw.githubusercontent.com/Akaswww/Machine-Learning/main/titanic.csv"
df = pd.read_csv(url)
print(df.head())
