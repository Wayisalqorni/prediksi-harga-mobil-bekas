import streamlit as st
import pandas as pd

df = pd.read_csv('toyota.csv')

st.title('Deskripsi Dataset Mobil Toyota')
sidebar_options = ['Deskripsi Data','Prediksi']
sidebar_choice = st.sidebar.selectbox('Pilihan', sidebar_options)
# Deskripsi Data
if sidebar_choice == 'Deskripsi Data':
    st.header('Deskripsi Data')
    st.write(df.head())