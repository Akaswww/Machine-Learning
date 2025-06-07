# IN THIS one we check what th efect of standarlization during model training we use
# standarization in many algo like lOgistic Regression , KNN , k-means, PCA, ANN, Gradient descent
# But in decision trees standarization not affect the model accuracy 
# i check it one by one see_--------


import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day24-standardization/Social_Network_Ads.csv"
df = pd.read_csv(url)
df=df.iloc[:,2:]

print(df.head())
# print(df.shape) =>  (400, 5)

X_train,X_test,Y_train,Y_test=train_test_split(df.drop('Purchased',axis=1),df['Purchased'],test_size=0.3,random_state=0)
# we usse axis=1 to drop column  and for deop row we used axis=0

# print(X_train.shape)  (280, 2)
# print(X_test.shape)   (120, 2)

sc = StandardScaler()  # create an instance

sc.fit(X_train)                # fit only on training data
sc_X_train = sc.transform(X_train)  # transform training data
sc_X_test = sc.transform(X_test)    # transform test data

# print(sc_X_train) it returns an array 
# to solve this problem we need make that array in a dataframe

sc_X_train=pd.DataFrame(sc_X_train,columns=X_train.columns)
sc_X_test=pd.DataFrame(sc_X_test,columns=X_test.columns)

print(sc_X_train.head())
print(sc_X_test.head())
print(sc_X_train.shape)  #(280, 2)
print(sc_X_test.shape)   #(120, 2)

# TO know in real scaling is done check theri mean and standard deviation mean is 0 and std is 1

print(np.round(sc_X_train.describe(),1))  # after scaling mean=0  and  standardeviation=1.
print(np.round(X_train.describe(),1))  #before scaling mean  37.9  69807.1 and std  10.2  34641.2


#  see in graph
#before scale
plt.figure(figsize=(8,8))
plt.title("After Scaling")
sns.scatterplot(data=sc_X_train,x='Age',y='EstimatedSalary',sizes=0.5)
plt.show()

# After scale
plt.figure(figsize=(8,8))
plt.title("Before Scaling")
sns.scatterplot(data=X_train,x='Age',y='EstimatedSalary',sizes=0.5)
plt.show()
 
# now compare the performance after and before scaling
lr=LogisticRegression()         #before scaling
lr_scale=LogisticRegression()   #after scaling

lr.fit(X_train,Y_train)
lr_scale.fit(sc_X_train,Y_train)

Y_pred=lr.predict(X_test)
Y_scale_pred=lr_scale.predict(sc_X_test)

print("Before scaling",accuracy_score(Y_test,Y_pred))
print("After scaling",accuracy_score(Y_test,Y_scale_pred))


