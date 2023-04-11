import streamlit as st
from deskripsi_mobil import function1
from estimasi_mobil import function2

# Menambahkan konten di sidebar
with st.sidebar:
    st.title('Pilihan')

    # Menambahkan konten dari file pertama
    st.subheader('Deskripsi')
    function1()

    # Menambahkan konten dari file kedua
    st.subheader('Prediksi')
    function2()

