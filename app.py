import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="My City Temperature Dashboard", layout="wide")
st.title("My City Temperature Dashboard")
df = pd.read_csv("daily_log.csv", skipinitialspace=True)
df["datetime"] = pd.to_datetime(df["time"])
df = df.sort_values("datetime")

max_idx = df["temp_f"].idxmax()
min_idx = df["temp_f"].idxmin()
