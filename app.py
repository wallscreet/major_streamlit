import streamlit as st

# --- Pages Setup ---
admin_dashboard = st.Page(
    page="views/admin_dashboard.py",
    title="Admin Dashboard",
    icon=":material/dashboard:",
)
sales_dashboard = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/team_dashboard:",
    default=True,
)


pg = st.navigation(
    {
        "Admin": [admin_dashboard],
        "Sales": [sales_dashboard],   
    }
)

pg.run()