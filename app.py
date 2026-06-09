import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df=pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Data Visualization')

selected_state=st.sidebar.selectbox('Select a State',list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')

if plot:
    st.text('size represent primary parameter')
    st.text('colour represent secondary parameter')
    if selected_state=='Overall India':
        #plot for indis
        fig = px.scatter_map(df, lat='Latitude', lon='Longitude',size=primary,color=secondary,color_continuous_scale='YlOrRd', zoom=4, map_style='carto-positron',width=1200,height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        #plot for state
        state_df=df[df['State']==selected_state]
        fig = px.scatter_map(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary,color_continuous_scale='YlOrRd', zoom=6,
                             map_style='carto-positron', width=1200, height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
