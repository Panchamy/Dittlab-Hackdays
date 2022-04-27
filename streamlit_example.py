import streamlit as st
import json
import plotly.express as px

#Description
sidebar = st.sidebar
sidebar.title('Streamlit example')
sidebar.write(
"""
This application is a simple example of dashboarding for uploading and visualising NDW data.  
You can find the streamlit cheatsheet here: https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py  
"""
)

#File uploader
uploaded_file = st.file_uploader('Select data to visualise')

if uploaded_file is not None:
    text = uploaded_file.read()
    data = json.loads(text)
    if data is not None:
        #Radio button
        select = st.radio('Visualise', ['speed', 'flow'])
        if select == 'speed':
            fig = px.imshow(data['speed'], x=data['t'], y=data['x'], zmin=0, 
                color_continuous_scale='blackbody', origin='lower',
                labels=dict(x="Time", y="Space", color="Speed (km/hr)"))
        if select == 'flow':
            fig = px.imshow(data['flow'], x=data['t'], y=data['x'], zmin=0, origin='lower',
                labels=dict(x="Time", y="Space", color="Flow (vehicles/lane/hr)"))
        st.plotly_chart(fig)     