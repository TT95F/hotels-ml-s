import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import streamlit as st
import pandas as pd
from hotels_ml.config import RAW_DIR
from hotels_ml.data_io import load_csv

st.set_page_config(page_title="Hotels — Explorer", layout="wide")

df = load_csv(RAW_DIR / "hotels.csv")

st.title("🏨 Hotels — Exploration")
left, right = st.columns([2,3])

with left:
    st.metric("Lignes", len(df))
    st.write("Colonnes:", len(df.columns))
    st.write("Aperçu")
    st.dataframe(df.head(20))

with right:
    st.write("Taux d'annulation par mois (si colonnes présentes)")
    if {"arrival_date_month","is_canceled"} <= set(df.columns):
        series = df.groupby("arrival_date_month")["is_canceled"].mean().sort_index()
        st.bar_chart(series)
    else:
        st.info("Colonnes manquantes pour cet aperçu.")
