import streamlit as st
import pandas as pd
from pprint import pprint
from millify import millify
import plotly.express as px

st.set_page_config(layout="wide")
st.title("2708 Statistics")
df = pd.read_csv("kvk.csv")
df = df.set_index("name")


def clean_stats(x):
    if isinstance(x, str):
        if "," in x:
            x = float(x.replace(",", "."))
        else:
            x = float(x.replace(".", ""))
    return x


stats = df.applymap(clean_stats)
all_names = stats.index.values
selected_name = st.selectbox("Select a player", all_names, placeholder="")
selected_player = stats.loc[selected_name].to_dict()
for key, value in selected_player.items():
    if isinstance(value, str):
        value = value.replace(",", ".")
        selected_player[key] = float(value.replace(".", ""))
pprint(selected_player)


with st.container():
    cols = st.columns(6)
    cols[0].metric(label="Rank", value=int(selected_player["no"]))
    cols[1].metric(
        label="Total Score",
        value=millify(selected_player["total_score"]),
        # delta="10%",
    )
    cols[2].metric(
        label="Total Kill Points",
        value=millify(selected_player["total_kill_points"]),
        # delta="30%",
    )
    cols[3].metric(
        label="Total Dead Points",
        value=millify(selected_player["total_dead_points"]),
        help="Total dead points calculated based on dead T4 and T5 troops",
        # delta="-40%",
    )

stats["size"] = 1


fig = px.scatter(
    stats,
    x="total_kill_points",
    y="total_dead_points",
    size="performance_index",
    hover_name=stats.index,
    title="Total Kill Points vs Total Dead Points",
    labels={
        "total_kill_points": "Total Kill Points",
        "total_dead_points": "Total Dead Points",
    },
)
with st.container():
    st.plotly_chart(fig, use_container_width=True)
