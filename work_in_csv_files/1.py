# u need some libraries to run all this code e.g
import pandas as pd
import numpy as np


# read the csv file if it is in same folder
df = pd.read_csv('titanic.csv')

# # if u getting error while import the data set sometimes u get those dataset whose encoding is different means the language,emoji dataset and all for reading those files
#  u need to know which encoding is used in those csv files then write this code 
df1=pd.read_csv('titanic.csv',encoding='which encoding is this')  #encoding=Latin-1 or etc


# if u getting error while import the data set which having some bad lines data or irregualr data so u can just write 
df2=pd.read_csv('titanic.csv',sep=';',error_bad_lines=False)

# to use specific columns u can use
df=pd.read_csv('titanic.csv',usecols=['PassengerId','Survived','Pclass'])



# to skip some rows
df=pd.read_csv('titanic.csv',skiprows=[0,3]) 

# print first 5 row
print(df.head())


# if u want to print some random rows not first 
print(df.sample())



# if u want the shape (rows,column)  
print(df.shape) #this is the  output u get(891, 12)



# if u want to to change the column datatype to other datatype e.g float to int
df=pd.read_csv('titanic.csv',dtype={'Cabin':int})



# if u want the to show which column which datatype
print(df.info())



# if u wnat to convert some large text in short form make a function then pass that function in the dictonary during reading csv files
def rename(name):
    if name == 'Royal Challenger Bengluru':
        return 'RCB'
    
    else:
        return 'name'

df3=pd.read_csv('titanic.csv',converters={'team':rename})


# if u want to replace some val;ues
df4=pd.read_csv('titanic.csv',na_values=['Males'])  #it replaces all Male values from NA \
    
# if u want to divide the dataset into chunks
df5=pd.read_csv('titanic.csv',chunksize=100) #now the dataset is divides into 100-100 chunks


