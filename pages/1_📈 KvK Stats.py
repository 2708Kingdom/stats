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


def calculate_player_df(df):
    player_df = df.copy()
    asc_cols = ["power_loss"]
    desc_cols = [
        "total_kill_points",
        "total_dead_points",
        "performance_index",
        "total_score",
    ]
    for col in asc_cols:
        player_df[col + "_rank"] = player_df[col].rank(ascending=True)
    for col in desc_cols:
        player_df[col + "_rank"] = player_df[col].rank(ascending=False)
    for col in player_df.columns:
        player_df[col + "_pct"] = player_df[col].rank(pct=True)
    return player_df


def format_score_and_pct(data, field, name):
    value = data[field]
    if value > 1e9:
        value = try_millify(value, 2)
    else:
        if field == "performance_index":
            value = try_millify(value, 1)
        else:
            value = try_millify(value)
    rank = int(data[f"{field}_rank"])
    pct = round(data[f"{field}_pct"] * 100)
    if field == "power_loss":
        pct = 100-pct
    return {"Metric": name, "Value": value, "Rank": rank, "Percentile": pct}


def show_player_stats(df):
    with st.container():
        player_stats = df.to_dict()
        player_summary = []
        for field, field_name in zip(
            ["total_score", "total_kill_points", "total_dead_points", "performance_index", "power_loss"],
            ["Total Score", "Kill Points", "Dead Points", "Performance Index", "Power Loss"],
        ):
            player_summary.append(format_score_and_pct(player_stats, field, field_name))
        st.dataframe(
            pd.DataFrame(player_summary).set_index("Metric"), use_container_width=True
        )


df = load_and_clean_stats()
output_df = df.copy()
mill_df = millify_stats(df)
player_df = calculate_player_df(output_df.copy())

with st.container():
    show_accolades(output_df.reset_index())


with st.container():
    st.header("Individual Statistics", divider=True)
    player_selection = st.selectbox("Select a player", df.index)
    single_player_data = player_df.loc[player_selection]
    show_player_stats(single_player_data)


with st.container():
    st.header("All Statistics", divider=True)
    st.dataframe(mill_df, use_container_width=True)
