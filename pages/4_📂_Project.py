import streamlit as st

st.title("📂 My Projects")

projects = {
    "Ice Cream Shop Website": "A website project for selling ice cream products with menu and order page.",
    "Streamlit Calculator": "A calculator app with multiple functions like add, subtract, multiply, divide.",
    "Student Record System": "A simple system for managing student information."
}

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)