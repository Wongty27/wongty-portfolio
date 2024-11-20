import streamlit as st

st.set_page_config(
    page_title="AutoML"
)

# --- PAGE SETUP ---
home_page = st.Page(
    page="views/home.py",
    title="Home",
    icon="🏠",
)

dashboard_page = st.Page(
    page="views/dashboard.py",
    title="Dashboard",
    icon="📊",
)

eda_page = st.Page(
    page="views/eda.py",
    title="Explanatory Data Analysis",default=True
)

forecaster_page = st.Page(
    page="views/forecaster.py",
    title="Forecaster",
    
)

classifier_page = st.Page(
    page="views/classifier.py",
    title="Classifier",
)

detection_page = st.Page(
    page="views/detection.py",
    title="Object Detection",
)

llm_page = st.Page(
    page="views/llm.py",
    title="LLM",
)

# --- NAVIGATION SETUP (WITH SECTIONS) ---
pg = st.navigation(
    {
        "Home": [
            home_page,
            # dashboard_page
        ],
        "Analysis": [
            eda_page,
        ],
        # "ML": [
            # forecaster_page,
            # classifier_page,
            # detection_page,
            # llm_page
        # ],
    }
)

# st.sidebar.text("Built by WongTY")

pg.run()