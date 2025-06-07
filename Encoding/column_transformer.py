# in one hot encoding we do many codes npstack removes columns then add ohe n all
# but using column transformer we can add any encoding in differnent different column

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer


url="https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day28-column-transformer/covid_toy.csv"
df=pd.read_csv(url)
# print(df.head())


X_train,X_test,Y_train,Y_test=train_test_split(df.iloc[:,0:5],df.iloc[:,-1],test_size=0.2)

transformer=ColumnTransformer(transformers=[
    ('tnf1',SimpleImputer(),['fever']),
    ('tnf2',OrdinalEncoder(categories=[['Mild','Strong']]),['cough']),
    ('tnf3',OneHotEncoder(drop='first',sparse_output=False,),['gender','city'])
    ],remainder='passthrough',)

X_train=transformer.fit_transform(X_train)
# print(X_train[:5])
print(X_train.shape)

