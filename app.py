import streamlit as st
from src.extraction import load_data

st.ser_page_config(layout="wide")

def min ():
    df = load_data()
    st.dataframe(df)

if __name__ == '__main__':
    main()