import streamlit as st

with open('output/html_files/html_1.html', 'r', encoding='utf-8') as file:
    html_code = file.read()
    st.markdown(html_code, unsafe_allow_html=True)

