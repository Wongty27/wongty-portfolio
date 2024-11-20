import numpy as np
import polars as pl
import streamlit as st
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime

# user_input = st.text_input(label="Choose a ticker:")
with st.form("my_form"):
    user_input = st.text_input(label="Choose a ticker:", key="ticker")
    submit_btn = st.form_submit_button(label="Submit")

if user_input and submit_btn:
    data = yf.download(tickers=user_input, ignore_tz=True)
    df = pl.from_pandas(data, include_index=True)
    st.write(df.tail())

    fig = px.line(df, x="Date", y="Adj Close", title="Historical Stock Price")
    st.plotly_chart(fig, use_container_width=True)


elif submit_btn and not user_input: 
    st.write("Please enter a valid :red[ticker symbol].")
