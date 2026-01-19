import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is your first deployed app.")

name = st.text_input("What's your name?")
st.write(f"Hello, {name}")
