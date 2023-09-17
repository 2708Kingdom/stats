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
