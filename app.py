import streamlit as st


# --- Pages Setup ---
landing_page = st.Page(
    page="pages/landing_page.py",
    title="Landing Page",
    icon=":material/home:",
    default=True
)
customer_details = st.Page(
    page="pages/customer_details.py",
    title="Customer Details",
    icon=":material/person:",
)
product_details = st.Page(
    page="pages/product_details.py",
    title="Product Details",
    icon=":material/inventory_2:",
)
dashboard = st.Page(
    page="pages/dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:",
)
testing_page = st.Page(
    page="pages/testing_page.py",
    title="Testing Page",
    icon=":material/bug_report:",
)
login_page = st.Page(
    page="pages/login.py",
    title="Login Page",
    icon=":material/login:",
)

pg = st.navigation(
    {
        "Login": [login_page],
        "Landing": [landing_page],
        "Dashboard": [dashboard],
        "Customers": [customer_details],
        "Products": [product_details],
        "Testing": [testing_page],
    }
)

pg.run()