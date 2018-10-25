import pandas as pd
qtr=pd.read_csv('C:\\Users\\Tina Sun\\Desktop\\term3\\machine learning\\machine-learning\\qtr_CRSP.csv')
cds=pd.read_stata('C:\\Users\\Tina Sun\\Desktop\\term3\\machine learning\\machine-learning\\cds_spread5y_2001_2016.dta')
#make sure the gvkey of this two file are same
cds.gvkey.dtypes
qtr.columns = qtr.columns.str.lower()
qtr.gvkey.dtypes
cds.gvkey=cds.gvkey.astype('int64')
cds.gvkey.dtypes
cds
qtr
#creat a list for cds with all quarter
cds.mdate.dtypes
qtr.datadate.dtypes
m=cds['mdate'].dt.month 
y=cds['mdate'].dt.year
cds_qtr=list()
d=0
for m in cds.mdate:
    if str(m)>0 and str(m)<4:
        a=str(y)+'Q1'
    if str(m)>3 and str(m)<7:
        a=str(y)+'Q2'
    if str(m)>6 and str(m)<10:
        a=str(y)+'Q3'
    else:
        a=str(y)+'Q4'
    cds_qtr.append(a)
cds_qtr
cds_qtr=pd.Series(cds_qtr)
cds1 = cds.assign(datacqtr=cds_qtr.values)

#merge two dataframe
new=pd.merge(cds1, qtr, on=['gvkey', 'datacqtr'])










