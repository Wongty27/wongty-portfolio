import streamlit as st
from streamlit_ydata_profiling import st_profile_report
from ydata_profiling import ProfileReport
import pandas as pd
from pathlib import Path

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    file_type = Path(uploaded_file.name).suffix
    df = pd.read_csv(uploaded_file) if file_type == ".csv" else pd.read_excel(uploaded_file)

    pr = ProfileReport(
        df,
        title="Profiling Report",
        explorative=True,
        html={'style':{'full_width':True}}
    )

    st_profile_report(pr, navbar=True)