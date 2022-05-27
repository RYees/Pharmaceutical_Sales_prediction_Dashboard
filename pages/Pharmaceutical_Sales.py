from shutil import chown
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def app():
    st.write("User Overview Analysis")


    df = pd.read_csv('tellco_data.csv', index_col=0)
    df = df.astype(str)
    # st.dataframe(df)

    # Top 10 Handset type and the top 3 handset maufacturer
    col1, col2 = st.columns(2)
    ht = df["Handset Type"].value_counts().index.tolist()
    hdf = pd.DataFrame(ht, columns=['Handset'])

    hm = df["Handset Manufacturer"].value_counts().index.tolist()
    mdf = pd.DataFrame(hm, columns=['Handset Manufacturer'])

    with col1:
        st.header("Top 10 Handsets")
        st.write(hdf[:10])
    st.markdown("""<span style="margin-left:50px;"></span>""", unsafe_allow_html=True)  
    with col2:
        st.header("Top 3 Handset Manufacturers")
        st.write(mdf[:3])

    st.markdown("""<span style="margin-top:100px;"></span>""", unsafe_allow_html=True)  

    st.header('Graph of Handset Type Vs Handset Manufacturer')
    
    # Manu_grp = df.groupby(["Handset Manufacturer"])
    # figure(figsize=(18,6))
    # plt.xlabel("Handset Manufacturer")
    # plt.ylabel("Handset Type Count")
    # fig = Manu_grp['Handset Type'].value_counts().loc['Apple'].head(5).to_frame()
    # # st.pyplot(fig)
    
    chart_data = pd.DataFrame(
    np.random.randn(50, 2),
    columns=["Handset Type", "Handset Manufacturer"])

    st.bar_chart(chart_data)

    # import plotly.express as px
    # import plotly.graph_objs as go

    # #create a canvas for each item
    # interactive =  st.beta_container()
    # all_columns_names= df.columns.tolist()
    # selected_column_names = st.multiselect("select column to plot",all_columns_names)

    # s = df[selected_column_names[0]].str.strip().value_counts()


    # with interactive:
    #     fig = go.Figure()
    #     for name,group in df.groupby(selected_column_names[0]):
    #         trace =go.Histogram()
    #         trace.name = name 
    #         trace.x = group[selected_column_names[1]]
    #         fig.add_trace(trace)
    #     fig.show()

    ####### task1.1
    st.header('Number or XDr per user')
    Userstot_grp = df.groupby(["MSISDN/Number"])
    so = Userstot_grp["Bearer Id"].value_counts().to_frame()
    # data = pd.DataFrame(
    #     np.random.randn(50, 2),
    #     columns=["MSISDN/Number", "Bearer Id"])
    st.dataframe(so)
    # st.bar_chart(data)