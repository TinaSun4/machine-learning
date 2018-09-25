# dropna, fillna, describe, transpose, concat, merge, join, apply, sort_values, isnull, head, columns, read_csv, to_csv

# assignment: from WRDS download compustat quarterly data from 2000 to 2017 as a CSV file. Show the summary statistic 
# for each variable (# observations, # missing, mean, std, P25, Median, P75). Remove the columns with
# more than 50% missings. Show the results for remaining variables in a table and format the table as nice as you can.



#import csv
import pandas as pd
raw=pd.read_csv('C:\\Users\\Tina Sun\\Desktop\\term3\\machine learning\\11.csv')
raw.rename(columns={'at': 'assets-total', 'dltt': 'long term debt-total','intan':'intangible assets-total','icapt':'invested capital-total','invt':'inventories-total','ist':'investment securities-total','ivst':'short term invesments-total','lcat':'loan/claims/advances-total','lt':'liablities-total','pvt':'provisions-total','rvti':'reserves-total','dvt':'dividends-total','idit':'interest and related income-total','nit':'net item-total','revt':'revenue-total','txt':'income taxes-total','xt':'expense-total','fuset':'uses of funds total','tfva':'total fair value assets','tfvl':'total fair value liabilites','mkvalt':'market value-total-fiscal','uinvt':'inventories-utility','sale':'sales/turnover(net)','ni':'net income','ch':'cash'})

#print raw
#remove columns with 50% missing 
frac=len(raw)*0.5
raw.dropna(thresh=frac,axis=1)
#replace all NAN with 0s
#raw.fillna('-')
raw.sort_values(by='gvkey', ascending=True)
table=raw.describe()
print table

