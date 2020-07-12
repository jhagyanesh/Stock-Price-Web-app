import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
""")
st.markdown("### 🎲 The Application")
st.markdown("This application is a Simple Stock Price App"
				" Shown are the stock **closing price** and ***volume*** of stocks!")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

f = open("symbols.txt", "r")
lines=f.read()
symList=lines.split("\n")
f.close()

symbol = st.sidebar.selectbox("Choose your symbol: ", symList)
years = st.slider("Choose time period in years: ", min_value=0, max_value=10, value=2, step=1)

#get data on this ticker
tickerData = yf.Ticker(symbol+'.NS')
#get the historical prices for this ticker
tickerDf = tickerData.history(period=str(years)+'y', interval='1d')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)