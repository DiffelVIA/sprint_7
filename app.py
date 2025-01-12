import pandas as pd
import streamlit as st
import plotly_express as px
car_data = pd.read_csv('vehicles_us.csv')
st.header('Vehicles sales information')
hist_button = st.button('Construir un histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, user_container_width=True)
scatter_button = st.button('Construir un gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(car_data, x='odometer')
    st.plotly_chart(fig, user_container_width=True)