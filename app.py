import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Uso de herramientas de desarrollo de software')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Botón para el histograma
hist_button = st.button('Construir histograma')

# Casilla de verificación para el diagrama de dispersión
build_scatter = st.checkbox('Construir diagrama de dispersión')

# Lógica para el histograma (usando botón)
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Lógica para el diagrama de dispersión (usando casilla)
if build_scatter:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)