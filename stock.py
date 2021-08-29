import datetime
from pandas_datareader import data
from bokeh.plotting import show,figure,output_file

stock_first=datetime.datetime(2021,7,1)
stock_last=datetime.datetime.now()
df=data.DataReader(name="GOOG",data_source="yahoo",start=stock_first,end=stock_last)

def stock_stats(open,close):
    if open>close:
        stat='stk_inc'
    elif open<close:
        stat='stk_dec'
    else:
        stat='equal'
    return stat

df['Stats']=[stock_stats(o,c) for o,c in zip(df.Open,df.Close)]
df['Height']=abs(df.Open-df.Close)
df['Mid']=(df.Open+df.Close)/2

# print(df)

time_data=12*60*60*1000

candle=figure(x_axis_type='datetime',width=1000,height=750)
candle.title="Google Stock"
candle.grid.grid_line_alpha=0.5

candle.segment(df.index,df.High,df.index,df.Low,color='black')
candle.rect(df.index[df.Stats=="stk_inc"],df.Mid[df.Stats=="stk_inc"],time_data,df.Height[df.Stats=="stk_inc"],fill_color='green',line_color='black')
candle.rect(df.index[df.Stats=="stk_dec"],df.Mid[df.Stats=="stk_dec"],time_data,df.Height[df.Stats=="stk_dec"],fill_color='red',line_color='black')

output_file('Google_Stock.html')
show(candle)