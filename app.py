import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config('wide')

df = pd.read_csv('india.csv')
list_states = list(df['State name'].unique())
list_states.insert(0, 'Overall India')

st.sidebar.title('India Census Data Viz')

selected_state = st.sidebar.selectbox('Select a state',list_states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size Represet Primary Parameter')
    st.text('color Represet Secondary Parameter')
    if selected_state == 'Overall India':
        # plot for India
        fig = px.scatter_mapbox(df, lat="lat", lon="long", hover_name="District name", size = primary, color = secondary,size_max=35, width=1200,height=700,
                        mapbox_style='carto-positron', zoom=4)
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        #plot for state
       state_df =  df[df['State name'] == selected_state]
       fig = px.scatter_mapbox(state_df, lat="lat", lon="long", hover_name="District name", size = primary, color = secondary,size_max=35, width=1200,height=700,
                        mapbox_style='carto-positron', zoom=6)
       st.plotly_chart(fig, use_container_width=True)
    