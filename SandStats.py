import streamlit as st
from utils.utilities import set_logos


st.set_page_config(layout="wide")
set_logos()
st.title("Analyze 'em all!")

st.header("How does it work?")
st.write("On Laboratory section you can upload your Showdown games to see some analysis.")
st.write("Only BO3 games can be uploaded to see all your data.")
st.write("It is recommended to upload all the games of the same team to analyze and understand the data optimally.")
st.write("Any data is stored on the server, all the games are erased when you refresh the page!")
st.text("")
st.text("")
st.text("")
st.write("I hope you find it useful and welcome any suggestions for improvement for future features. You can find me on [X](https://x.com/wilreg358022).")
st.write("Sandstats is on alpha version, new sections will be added!")


