#For assignment 2, use "compustat_annual_2000_2017_with link information" to build a model 
#to predict operational profit. At the top of your code, how you calculate the operational profit.

#import excel
import pandas as pd
raw=pd.read_csv('C:\\Users\\Tina Sun\\Desktop\\term3\\machine learning\\machine-learning\\compustat_annual_2000_2017_with link information.csv')
#remove columns with 70% missing and non-numeric variables
frac=len(raw)*0.3
raw1=raw.dropna(thresh=frac,axis=1)
raw2=raw1._get_numeric_data()
raw3=pd.DataFrame(data=raw2)
#fill missing value with median
raw4=raw3.fillna(raw.median())
raw4
'''writer=pd.ExcelWriter('C:\\Users\\Tina Sun\\Desktop\\term3\\machine learning\\machine-learning\\11.xlsx')
raw4.to_excel(writer,'Sheet1')
writer.save()'''

# write a function that runs skLearn linear_model iteratively


# and at each iteration goes through stepwise process to choose the variables.
# Use a level of significance of 0.05 for critical value.
# Use your function to build a linear model on the dataset that will be emailed to you. 
# Before building the model,impute all missing values to the median of that variable and cap and floor outliers at 0.1% and 99.9%.