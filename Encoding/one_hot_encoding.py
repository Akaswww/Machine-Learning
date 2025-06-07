import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


url = "https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day27-one-hot-encoding/cars.csv"
df = pd.read_csv(url)
# print(df.head())

# we can do one hot encoding using pandas
df1=pd.get_dummies(df,columns=['fuel','owner'])
# print(df.head())  we not usw pandas in ML Projects because it dosent learn the order of columns

# we used onehotencoding in scikitlearn

X_train,X_test,Y_train,Y_test=train_test_split(df.iloc[:,0:4],df.iloc[:,-1],test_size=0.2,random_state=42)

ohe=OneHotEncoder(drop='first',sparse=False,dtype=np.int32)  #use this encoder this encoder encodes entire dataframe to one hot encoding 
#                     so that is why we divide the columns where we want to put this encoder then we will join them with original dataframe.

X_train_new=ohe.fit_transform(X_train[['fuel','owner']])
X_test_new=ohe.transform(X_test[['fuel','owner']])

# now add these in new dataframe
np.hstack((X_train[['brand','km_driven']].values,X_train_new))
print(df.head())