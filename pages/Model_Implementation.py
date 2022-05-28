import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from scipy.stats import skew

# import matplotlib.pylab as plts
import seaborn as sns
# from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import Normalizer
# import sklearn.cluster as cluster
# from sklearn import preprocessing
# from sklearn.cluster import KMeans


def app():
    # df = pd.read_csv('tellco_data.csv', index_col=0)
    # df = df.astype(str)
    # print(df)
    # st.dataframe(df)

    st.title('Explore the Data-set')
    # st.dataframe(df.describe())
    st.markdown('### Analysing column relations')
    st.text('Correlations:')
    # fig, ax = plt.subplots(figsize=(10,10))
    # sns.heatmap(df.corr(), annot=True, ax=ax)
    # st.pyplot(fig)
    # st.text('Effect of the different classes')
    # fig = sns.pairplot(df, vars=['Bearer Id', 'Dur. (ms)', 'Total DL (Bytes)'], hue='Start')
    # st.pyplot(fig)