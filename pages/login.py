import streamlit as st
from modules.auth import cookie_manager, authenticate_user
import extra_streamlit_components as stx
from time import sleep
import json

# Retrieve the cookie and parse it correctly
cookie = cookie_manager.get("majorsupply")
if cookie:
    try:
        cookie = json.loads(cookie)  # Convert JSON string back to dictionary
        if cookie.get("authenticated", True):
            st.switch_page("pages/landing_page.py")
    except json.JSONDecodeError:
        cookie = {}  # Handle case where cookie is not a valid JSON string
else:
    cookie = {}

st.dialog("Login")
def login_form():
    st.subheader('🔑 Login')
    _username = st.text_input('Username')
    _password = st.text_input('Password', type='password')
    login_button = st.button('Login')

    if login_button:
        authenticated, _role = authenticate_user(_username, _password)
        if authenticated:
            st.success(f'✅ Welcome, {_username}! You are logged in as a {_role}.')
            cookie_value = {"authenticated": True, "username": _username, "role": _role}
            cookie_manager.set("majorsupply", json.dumps(cookie_value))  # Store as JSON string
            sleep(2)
            st.switch_page("pages/landing_page.py")  # Reload the page after setting the cookie

        else:
            st.error('❌ Invalid username or password.')

# Run login form
login_form()


