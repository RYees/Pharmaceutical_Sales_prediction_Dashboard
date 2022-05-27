import streamlit as st
import pandas as pd
from multiapp import MultiApp
from pages import Pharmaceutical_Sales
# import numpy as np
# import plotly.express as px

<<<<<<< HEAD
st.header("Analysis for Pharmaceutical Sales Prediction")
=======
st.header("Analysis for Telecommunication Industry")
>>>>>>> e676ed32bf8fba127a4c758bfe7f8d7209dd9674

# st.write(df)

# st.set_page_config(page_title="TellCo Telecom Analytics", layout="wide")

app = MultiApp()

PAGES = {
    "Pharmaceutical Sales": Pharmaceutical_Sales
}

st.sidebar.markdown("""
# Pharmaceutical Sales prediction
### Explore
""")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

# Add all your application here
# app.add_app("User Overview Analysis", User_Overview_Analysis.app)
# app.add_app("User Engagement Analysis", User_Engagement_Analysis.app)
# app.add_app("User Experience Analysis", User_Experience_Analysis.app)
# app.add_app("User Satisfaction Analysis", User_Satisfaction_Analysis.app)
# app.add_app("Predict Satisfaction", Model_Implementation.app)

# # The main app
# app.run()