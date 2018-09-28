#import excel
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
raw=pd.read_csv('C:\\Users\\Tina Sun\\Desktop\\term3\\machine learning\\machine-learning\\compustat_annual_2000_2017_with link information.csv')
#remove observations with missing operational profit (Y variable). 
raw1=raw.dropna(subset=['oiadp'])
raw2=pd.DataFrame(data=raw1)
raw2=raw2._get_numeric_data()
print raw2

'''
Find attribute to spilt at the best node(as pure as possible),
 which give the highest gain/gain ratio
'''
'''
X=raw2.values[:,1:5]
Y=raw2.values[:,500]

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)
#Decision Tree Classifier with criterion gini index
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=4, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)
#Decision Tree Classifier with criterion information gain
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=4, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)
#Prediction for Decision Tree classifier with criterion as gini index
y_pred = clf_gini.predict(X_test)
y_pred
'''

    
    
    
    
    
    
    
    