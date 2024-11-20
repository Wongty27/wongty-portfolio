import polars as pl
from pathlib import Path
import streamlit as st

@st.fragment
def download_function(data):
    st.download_button(
        label="Download data as csv",
        data=data,
        file_name="result.csv",
    )

def file_reader(uploaded_file):
    file_type = Path(uploaded_file.name).suffix
    match file_type:
        case ".csv":
            return pl.read_csv(uploaded_file)
        case ".xlsx":
            return pl.read_excel(uploaded_file)
        case ".parquet":
            return pl.read_parquet(uploaded_file)

def data_cleaning(df) -> pl.DataFrame | pl.LazyFrame:
    df = df.with_column(pl.col("Date").str.strptime(pl.Datetime, format="%Y-%m-%d"))
    return df