"""
Aplicación Web de Análisis Exploratorio de Datos de Ventas de Autos

Esta aplicación web desarrollada con Streamlit permite realizar un análisis
exploratorio interactivo de un conjunto de datos de anuncios de venta de coches.
Funcionalidades principales:
- Visualización de histogramas interactivos
- Creación de gráficos de dispersión
- Análisis exploratorio de datos de vehículos
"""

import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header("Análisis Exploratorio de Datos de Ventas de Autos")

# crear un botón de histograma
hist_checkbox = st.checkbox('Construir histograma')

# al hacer clic en el botón
if hist_checkbox:
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches'
    )

    # crear un histograma
    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del kilometraje",
        labels={
            "odometer": "Odómetro (millas)"
        }
    )
    fig.update_layout(
        yaxis_title="Cantidad de vehículos"
    )
    fig.update_layout(title_x=0.5)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear un botón de grafico de dispersión
disp_checkbox = st.checkbox('Construir gráfico de dispersión')

# al hacer clic en el botón
if disp_checkbox:
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches'
    )

    # crear un gráfico de dispersión
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre el kilometraje y el precio del vehículo",
        labels={
            "odometer": "Odómetro (millas)",
            "price": "Precio (USD)"
        }
    )
    fig.update_yaxes(range=[0, 200000])
    fig.update_layout(title_x=0.5)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
