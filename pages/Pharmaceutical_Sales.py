import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pickle
import seaborn as sns
# with open('rf_model.plk', 'wb') as f:
#   pickle.dump(rf, f)
# with open('rf_model.plk', 'rb') as f:
#     mf = pickle.load(f)
import time
from PIL import Image

def app():
    # st.write("Pharmaceutical Sales Prediction")
 
    st.markdown("""<span style="margin-top:100px;"></span>""", unsafe_allow_html=True)  

    uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file with the following 'Date', 'IsHoliday','IsWeekend','IsPromo' column names.", type=['csv', 'xlsx'])
    
    # lstm_model = open("..model/istm_model.pkl","rb")
    # lstm_model = pickle.load(lstm_model)
    
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
        fig = plt.figure(figsize=(10, 4))
        sns.lineplot(x = "Month", y = "Sales", data = df)
        st.pyplot(fig)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application")

    st.header('Pharmaceutical Sales prediction sales amount and number of customers')
   