#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:21:08 2022

@author: namnguyen
"""

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
        #Simple Stock Price App
        Shown are the stock ***closing price*** and ***volume*** of Google
        
        """)
        
tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d', start='2020-1-01', end='2022-11-30')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)