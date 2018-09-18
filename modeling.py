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
#raw4

# write a function that runs skLearn linear_model iteratively
# and at each iteration goes through stepwise process to choose the variables.
# Use a level of significance of 0.05 for critical value.
# Use your function to build a linear model on the dataset that will be emailed to you. 
import statsmodels.api as sm
X = raw4.loc[:,raw4.columns!='oiadp']
y = raw4['oiadp']
def stepwise(X,y,          
             initial_list=[],
             threshold_in=0.05,
             threshold_out=0.05,
             verbose=True):
    included=list(initial_list)
    while True:
        changed=False
        #forward step
        excluded=list(set(X.columns)-set(included))
        new_pval=pd.Series(index=excluded)
        for new_column in excluded:
            model=sm.OLS(y,sm.add_constant(pd.DataFrame(X[included+[new_column]]))).fit()
            new_pval[new_column]=model.pvalues[new_column]
        best_pval=new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.argmin()
            included.append(best_feature)
            changed= True
            if verbose:
                print('Add {:30} with p-value{:.6}'.format(best_feature,best_pval))
       #backward step
        model=sm.OLS(y,sm.add_constant(pd.DataFrame(X[included]))).fit()
        #use all coefs except intercept
        pvalues=model.pvalues.iloc[1:]
        worst_pval=pvalues.max()
        if worst_pval > threshold_out:
            changed=True
            worst_feature=pvalues.argmax()
            included.remove(worst_feature)
            if verbose:
                print('drop {:30} with p=value{:.6}'.format(worst_feature,worst_pval))
        if not changed:
            break
        return included
result=stepwise(X,y)
print('operational profits:')
print(result)


