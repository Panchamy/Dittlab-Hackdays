import streamlit as st
import json
import plotly.express as px

sidebar = st.sidebar
sidebar.title('Streamlit example')
sidebar.write(
"""
This application is a simple example of dashboarding for uploading and visualising NDW data.  
You can find the streamlit cheatsheet here: https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py  
"""
)

uploaded_file = st.file_uploader('Select data to visualise')

if uploaded_file is not None:
    # read file
    text = uploaded_file.read()
    data = json.loads(text)
        