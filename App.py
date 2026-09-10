import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, welcome to my first Streamlit application!")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"Hello, {name}! Nice to meet you.")