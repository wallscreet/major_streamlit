import streamlit as st
import extra_streamlit_components as stx
from modules.auth import cookie_manager
import json

st.title("Landing Page")

cookie = cookie_manager.get("majorsupply")
if cookie:
    try:
        cookie = json.loads(cookie)  # Convert JSON string back to dictionary
    except json.JSONDecodeError:
        cookie = {}  # Handle case where cookie is not a valid JSON string
else:
    cookie = {}

if cookie.get("authenticated") != True:
    st.write("You must be logged in to view this page...")
    login_button = st.button("Login")
    if login_button:
        st.switch_page("pages/login.py")

else:
    st.subheader(f"Welcome, {cookie['username']}!")
    logout_button = st.sidebar.button("Logout")
    if logout_button:
        cookie_manager.delete("majorsupply")

