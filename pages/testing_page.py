from datetime import datetime, timedelta
import json
import streamlit as st
import bcrypt
import yaml
from modules.auth import load_users, authenticate_user, hash_password, verify_password, registration_form, login_form
import extra_streamlit_components as stx


def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()
major_cookie = cookie_manager.get("majorsupply") or None

if major_cookie:
    st.session_state.username = major_cookie["username"]
    st.session_state.role = major_cookie["role"]
    st.session_state.authenticated = True

if "authenticated" not in st.session_state:
    st.write("Not Authenticated")
else:
    st.write(st.session_state.authenticated)

with st.expander("Cookies"):
    st.write(major_cookie)
    st.write(f"Session State: {st.session_state}")
    
    delete_cookie_input = st.text_input("Cookie Name")
    delete_cookie_button = st.button("Delete Cookie")
    if delete_cookie_button:
        cookie_manager.delete(delete_cookie_input)


with st.expander("Auth Testing and Hashing"):
    st.text_input("New Password", key="new_pass")
    if st.session_state.get("new_pass"):
        st.write("New Password Hash: ", hash_password(st.session_state.new_pass))
    
    # Streamlit UI
    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="pass_input")

    users = load_users().get("users", {})

    if st.session_state.get("username") in users:
        stored_password = users[st.session_state.username]["password"]
        st.write(f"Stored Password: {stored_password}")
        try:
            st.session_state.authenticated = verify_password(stored_password, st.session_state.pass_input)

        except Exception as e:
            st.error(f"Error: {e}")


with st.expander("Registration Form"):
    registration_form()
    #st.write(cookies)
    
with st.expander("Login Form"):
    authenticated, role = login_form()
    st.write(f"Authenticated: {authenticated}, Role: {role}")

logout_button = st.button("Logout")

if logout_button:
    if major_cookie:
        cookie_manager.delete("majorsupply")
    st.session_state.username = None
    st.session_state.role = None
    st.session_state.authenticated = False
    