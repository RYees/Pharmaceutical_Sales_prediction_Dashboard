from distutils.command.upload import upload
from shutil import chown
from itsdangerous import exc
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def app():
    # st.write("Pharmaceutical Sales Prediction")

    st.markdown("""<span style="margin-top:100px;"></span>""", unsafe_allow_html=True)  

    uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file with the following 'Date', 'IsHoliday','IsWeekend','IsPromo' column names.", type=['csv', 'xlsx'])
    
    global df
    if uploaded_file is not None:
        print(uploaded_file)
        try:
            df = pd.read_csv(uploaded_file) 
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)
    try:
        st.write(df)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application")

    st.header('Pharmaceutical Sales prediction sales amount and number of customers')
   