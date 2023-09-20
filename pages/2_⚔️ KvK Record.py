import streamlit as st
import pandas as pd
from utils.data import load_and_clean_stats, millify_stats, try_millify
import plotly.express as px

LOGO_PATH = "assets/logo.png"

st.set_page_config(
    page_title="EvoX - KvK Record",
    page_icon=LOGO_PATH,
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(LOGO_PATH, width=125)
st.title("⚔️ KvK Record ⚔️")

st.markdown("""
    ### KvK 6 👑 ⭐
    - Seed: B
    - Allies: 2825, 2709, 2679, 2784, 2824
            
    ### KvK 5 ❌
    - Seed: C
    - Allies: 1920, 2473, 1213, 1327
            
    ### KvK 4 👑
    - Seed: C
    - Allies: 1348, 1445, 2725, 1696, 2453, 2416, 2692
            
    ### KvK 3 👑
    - Seed: B
    - Allies: 2707, 2710, 2691, 2711 
    - Opponents: 2717, 2715, 2696

    ### KvK 2 ❌
    - Seed: A
    - Allies: 2714, 2691, 2696
    - Opponents: 2717, 2707, 2702, 2693

    ### KvK 1 👑
    - Allies: 2707, 2706, 2709
    - Opponents: 2710, 2711, 2712

    """)