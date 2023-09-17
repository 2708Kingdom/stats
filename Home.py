import streamlit as st
from utils.constants import LOGO

st.set_page_config(
    page_title="EvoX - Home",
    page_icon=LOGO,
    initial_sidebar_state="expanded"
    )
st.image(LOGO, width=125)
st.title("Kingdom 2708 – EvoX")
st.caption("*Sid is nüb*")

def about():
    st.header("About EvoX")
    st.write("""
    EvoX is Kingdom 2708's primary alliance in Rise of Kingdoms. We are a group of experienced players who have come together to create a competitive, yet fun environment. 

    We are a family and we look out for each other. We fight fiercely for our kingdom and our allies and we **NEVER** back down from a fight.

    **We are EvoX.**
    """)

def apply():
    st.header("Apply for Migration")
    st.markdown("""
        To apply for Kingdom 2708, 
                please join our 2708 Recruits Discord Server and submit the necessary items. A member of our leadership will be there to guide you through the process. We look forward to reviewing your application!
    """
    )            
    st.markdown("[Join us on Discord](https://discord.gg/y3ESpkSc)")

about()
apply()

# df = pd.read_csv("stats.csv")
# df = df.set_index("name")
# stats = df.applymap(clean_stats)

# kd_tab, individual_tab = st.tabs(["Kingdom Statistics", "Individual Statistics"])

# kd_stats = stats.reset_index()


# def write_accolade(col, field, accolade):
#     stat = kd_stats[kd_stats[field] == kd_stats[field].max()].iloc[0].to_dict()
#     col.metric(
#         label=f"{accolade}: {millify(stat[field])}",
#         value=stat["name"],
#     )


# with kd_tab:
#     cols = st.columns(4)
#     write_accolade(cols[0], "total_score", "Highest Total Score")
#     write_accolade(cols[1], "total_kill_points", "Most Kill Points")
#     write_accolade(cols[2], "total_dead_points", "Most Dead Points")
#     write_accolade(cols[3], "performance_index", "Highest Performance Index")

#     fig = px.scatter(
#         stats,
#         x="total_kill_points",
#         y="total_dead_points",
#         size="performance_index",
#         hover_name=stats.index,
#         title="Total Kill Points vs Total Dead Points",
#         labels={
#             "total_kill_points": "Total Kill Points",
#             "total_dead_points": "Total Dead Points",
#         },
#     )
#     with st.container():
#         st.plotly_chart(fig, use_container_width=True)

# with individual_tab:
#     all_names = stats.index.values
#     selected_name = st.selectbox("Select a player", all_names, placeholder="")
#     selected_player = stats.loc[selected_name].to_dict()

#     with st.container():
#         cols = st.columns(6)
#         cols[0].metric(label="Rank", value=int(selected_player["no"]))
#         cols[1].metric(
#             label="Total Score", value=millify(selected_player["total_score"])
#         )
#         cols[2].metric(
#             label="Total Kill Points",
#             value=millify(selected_player["total_kill_points"]),
#         )
#         cols[3].metric(
#             label="Total Dead Points",
#             value=millify(selected_player["total_dead_points"]),
#             help="Total dead points calculated based on dead T4 and T5 troops",
#         )
#         if "sid" in selected_name.lower():
#             st.image(
#                 "https://lumiere-a.akamaihd.net/v1/images/ct_iceage_sid_21464_10f2d363.jpeg",
#                 use_column_width=True,
#             )
#     stats["size"] = 1


# suggestion_box = st.text_input("Make a suggestion or leave your feedback here")
# if suggestion_box:
#     st.write("Fine why don't you do it then? :angry:")