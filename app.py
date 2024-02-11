import streamlit as st
import yfinance as yf
# import pandas as pd
# import numpy as np
import cufflinks as cf
import datetime
st.markdown('''
# STOCK VISION
A TRADER'S HANDBOOK           
made by krishna advaith siddhartha
            
`Shown are the stock price for query companies!`
- Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
''')
st.write('---')
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))
ticker_list = pd.read_csv('/Users/krishnaadvaithsiddhartharangavajjula/Documents/ml projects/constituents_symbols.txt' , sep = " ")
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list)
tickerData = yf.Ticker(tickerSymbol) 
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) 
string_name = tickerData.info['longName']
st.header('**%s**' % string_name)
if 'longBusinessSummary' in tickerData.info:
    string_summary = tickerData.info['longBusinessSummary']
    st.info(string_summary)
else:
    st.warning("No business summary available for this stock.")
st.info(string_summary)
st.header('**Ticker data**')
st.write(tickerDf)
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)
