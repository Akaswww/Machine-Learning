# ordinak encoding is used where the data is in the form of ordianl e.g. (poor,bad,good)=>(1,2,3)
#label endoing is always used in a output column not input


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder

url = "https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day26-ordinal-encoding/customer.csv"
df = pd.read_csv(url)
# print(df.head())

# we gonna add ordinal encoding in review and school and label in output column purchased

df=df[['review','education','purchased']]


X_train,X_test,Y_train,Y_test=train_test_split(df.iloc[:,0:2],df.iloc[:,-1],test_size=0.2)

oe=OrdinalEncoder(categories=[['Poor','Average','Good'],['School','UG','PG']])

X_train=oe.fit_transform(X_train)
X_test=oe.transform(X_test)

# convert in dataframe
X_train=pd.DataFrame(X_train,columns=['review', 'education'])
# print(X_train.head())

# Label encoding in purchased column is
le=LabelEncoder()
Y_train=le.fit_transform(Y_train)
Y_test=le.transform(Y_test)

print(pd.Series(Y_train).head())
