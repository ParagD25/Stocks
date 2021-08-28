import datetime
from pandas_datareader import data
from bokeh.plotting import show,figure,output_file

stock_first=datetime.datetime(2021,7,1)
stock_last=datetime.datetime.now()
df=data.DataReader(name="GOOG",data_source="yahoo",start=stock_first,end=stock_last)
print(df)