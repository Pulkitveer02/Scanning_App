import streamlit as st
import time
import random

st.set_page_config(page_title="Color Switcher", layout="wide")

COLOR_OPTIONS = [
    "red", "blue", "green", "yellow", "orange",
    "purple", "pink", "cyan", "black", "white"
]

st.sidebar.header("⚙️ Settings")

selected_colors = st.sidebar.multiselect(
    "Choose 2–5 Colours",
    COLOR_OPTIONS,
    default=["red", "blue"]
)

if len(selected_colors) < 2:
    st.sidebar.error("Please select at least 2 colours.")
if len(selected_colors) > 5:
    st.sidebar.error("You can select a maximum of 5 colours.")

switch_time = st.sidebar.number_input(
    "Time between changes (seconds)",
    min_value=0.5,
    max_value=10.0,
    value=2.0,
    step=0.5
)

st.title("📱 Colour Switcher App")
st.write("The background colour will keep changing based on your settings.")

placeholder = st.empty()

while True:
    if 2 <= len(selected_colors) <= 5:
        colour = random.choice(selected_colors)
        placeholder.markdown(
            f"""
            <div style='background-color:{colour};
                        width:100%;
                        height:90vh;
                        border-radius:10px;'>
            </div>
            """,
            unsafe_allow_html=True
        )
    time.sleep(switch_time)
