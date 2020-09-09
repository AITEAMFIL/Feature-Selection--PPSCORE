import pandas as pd
import seaborn as sns
import ppscore as pps
from pandas import ExcelFile

traindata = 'D://Download//traindata.xlsx'

df = pd.read_excel("D://Download//traindata.xlsx")

predictors_df = pps.predictors(df,y="label")

plot = sns.barplot(data=predictors_df, x="x", y="ppscore")
plot.set_xticklabels(plot.get_xticklabels(),rotation=90)
