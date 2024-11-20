import streamlit as st
import polars as pl
from pathlib import Path
from models import forecast, credit_risk
from utils.preprocess import download_function, file_reader

with st.form("my_form"):
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["csv", "xlsx", "parquet"]
    )

    if uploaded_file is not None:
        df = file_reader(uploaded_file)

    selected_task = st.selectbox(
        label="Select a task",
        options=[
            "Market Forecast",
            "Risk Modeling",
        ]
    )

    # match selected_task:
    #     case "Market Forecast":
    #         st.write("forecast")
    #         # result = forecast(df)
    #     case "Risk Modeling":
    #         # result = credit_risk(df)
    #         st.write("risk")

    submmitted = st.form_submit_button(label="Start EDA")

if submmitted:
    st.dataframe(df.tail())

# st.write(result)
    

# result = df.tail()


# download_function(data=result)