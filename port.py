import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai
import random

# --- Page Config ---
st.set_page_config(page_title="Sahil Desai | Portfolio", layout="wide", page_icon="\U0001F4BC")

# --- Theme Toggle ---
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

theme_toggle = st.toggle("\U0001F319 click here to chnage to Dark Mode", value=(st.session_state["theme"] == "dark"))
st.session_state["theme"] = "dark" if theme_toggle else "light"

# --- Apply Theme CSS ---
def apply_theme(theme):
    transition_css = """
    <style>
    .stApp {
        transition: background-color 0.6s ease, color 0.6s ease;
    }
    </style>
    """
    st.markdown(transition_css, unsafe_allow_html=True)

    if theme == "dark":
        st.markdown("""
            <style>
                body, .stApp { background-color: #1e1e1e; color: #ffffff; }
                .css-18e3th9, .css-1d391kg { background-color: #262730; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #ffffff !important; }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                body, .stApp { background-color: #ffffff; color: #000000; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #000000 !important; }
            </style>
            """, unsafe_allow_html=True)

apply_theme(st.session_state["theme"])

# rest of the code continues as is...
