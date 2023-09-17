import streamlit as st
import pandas as pd
from utils.data import load_and_clean_stats, millify_stats, try_millify
import plotly.express as px

LOGO_PATH = "assets/logo.png"

st.set_page_config(
    page_title="EvoX - KvK Stats",
    page_icon=LOGO_PATH,
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(LOGO_PATH, width=125)
st.title("KvK 6 Statistics")



def write_accolade(df, col, field, accolade):
    stat = df[df[field] == df[field].max()].iloc[0].to_dict()

    value = stat[field]
    if value > 1e9:
        value = try_millify(value, 2)
    else:
        if field == "performance_index":
            value = try_millify(value, 1)
        else:
            value = try_millify(value)
    col.metric(
        label=f"{accolade}: {value}",
        value=stat["name"],
    )


def show_accolades(df):
    st.header("Kingdom Accolades", divider=True)
    with st.container():
        cols = st.columns(4)
        for col, col_name, label in zip(
            cols,
            [
                "total_score",
                "total_kill_points",
                "total_dead_points",
                "performance_index",
            ],
            [
                "Highest Total Score",
                "Most Kill Points",
                "Most Dead Points",
                "Highest Performance Index",
            ],
        ):
            write_accolade(df, col, col_name, label)



df = load_and_clean_stats()
output_df = df.copy()
mill_df = millify_stats(df)
show_accolades(output_df.reset_index())
st.header("All Statistics", divider=True)
st.dataframe(mill_df, use_container_width=True)
