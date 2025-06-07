# elimante unit and convert in noraml numerical digit


# USING MIN-MAX scaling
# Formula:
     
#      X(i)= X(i)-X(min)/X(max)-X(min)  it is always sacled in [0,1]

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/a315efd557d2fc96984ded8f7f440af0320e6ae2/day25-normalization/wine_data.csv"
df = pd.read_csv(url)
# print(df.columns)



