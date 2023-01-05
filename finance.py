#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:21:08 2022

@author: namnguyen
"""
from datetime import datetime
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
        #Simple Stock Price App
        Shown are the stock ***closing price*** and ***volume*** of Google, Apple, Amazon, Twitter, Tesla
        
        """)
        
#tickerSymbol=['GOOGL','AAPL', 'AMZN', 'TWTR', 'TSLA' ]
tickerSymbol=['KIN','BONK']

for k in tickerSymbol:

    tickerData=yf.Ticker(k)
    tickerDf=tickerData.history(period='1d', start='2022-1-01', end= datetime.now().date())
    st.write(k)
    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
