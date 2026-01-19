import streamlit as st

name = st.text_input("What's your name?")
st.write(f"Hello, {name}")
