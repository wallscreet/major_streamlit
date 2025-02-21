import streamlit as st
import bcrypt
import yaml
from datetime import datetime, timedelta
import json
import extra_streamlit_components as stx
from time import sleep

cookie_manager = stx.CookieManager()

def get_manager():
    return stx.CookieManager()

# Load users from YAML file
def load_users():
    with open("users.yaml", "r") as file:
        return yaml.safe_load(file)

# Function to hash a password (only for new users)
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Function to verify password
def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password.encode())

# Function to authenticate a user
def authenticate_user(username, password):
    users = load_users().get("users", {})
    user = users.get(username)

    if user and verify_password(user["password"], password):
        return True, user["role"]
    return False, None


def add_user(username, name, email, password, role):

    users = load_users()
    if username in users["users"]:
        st.error("⚠️ Username already exists!")
        return
    hashed_pw = hash_password(password)
    users["users"][username] = {"name": name, "email": email, "password": hashed_pw, "role": role}
    with open("users.yaml", "w") as file:
        yaml.dump(users, file)
    st.success("✅ Registration successful! You can now log in.")

# Function to display the login form

# Function to display the registration form
def registration_form():
    st.subheader('📝 Register')
    new_username = st.text_input('Choose a Username')
    new_name = st.text_input('Your Name')
    new_email = st.text_input('Your Email')
    new_password = st.text_input('Choose a Password', type='password')
    new_role = st.selectbox('Select Role', ['admin', 'user'])
    register_button = st.button('Register')

    if register_button:
        if new_username and new_name and new_email and new_password:
            add_user(new_username, new_name, new_email, new_password, new_role)
        else:
            st.error('⚠️ Please fill in all fields.')