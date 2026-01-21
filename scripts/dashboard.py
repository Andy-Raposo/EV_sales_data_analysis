# app.py
import streamlit as st
import pandas as pd
from ev_viz import year_plot  # import your function from your scripts

# Load data
df = pd.read_csv("../data/processed/EV_car_sales.csv")  # same data you use in notebook

# Streamlit sidebar controls
countries = st.sidebar.multiselect(
    "Select countries:", 
    ['Germany', 'France', 'Spain', 'EU27'],
    default=['Germany', 'France', 'Spain', 'EU27']
)
powertrain = st.sidebar.selectbox("Select powertrain:", ["BEV", "PHEV", "FCEV"])
log_scale = st.sidebar.checkbox("Log scale")
title = st.sidebar.text_input("Chart title", "EV Sales in different regions")

# Call your plotting function
fig = year_plot(df, countries=countries, powertrain=powertrain, log=log_scale, title=title)
st.pyplot(fig)
