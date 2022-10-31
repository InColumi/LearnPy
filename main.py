import streamlit as st
import pandas as pd
import numpy as np

st.title('Лабораторная работа 4')

uploaded_file = st.file_uploader("Choose a photo")
if uploaded_file is not None:
    # To read file as bytes:
    with st.spinner('Wait for it...'):
        bytes_data = uploaded_file.getvalue()
        st.image(bytes_data)
    st.success('Done!')
    st.snow()