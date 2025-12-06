"""
Aplicación Web de Análisis Exploratorio de Datos de Ventas de Autos

Esta aplicación web desarrollada con Streamlit permite realizar un análisis
exploratorio interactivo de un conjunto de datos de anuncios de venta de coches.
Funcionalidades principales:
- Visualización de histogramas interactivos
- Creación de gráficos de dispersión
- Análisis exploratorio de datos de vehículos
"""

import os
import time

import streamlit as st
import pandas as pd
import plotly.express as px

# TITULO DE LA APLICACIÓN
st.header("Análisis Exploratorio de Datos de Ventas de Autos")


# CONFIGURACIÓN DE LA PÁGINA
if "archivo_cargado" not in st.session_state:
    st.session_state.archivo_cargado = False


# CONSTANTE ARCHIVO CSV
ARCHIVO = "vehicles_us.csv"


# VALIDACION DE LA CARGA DEL ARCHIVO
if not os.path.exists(ARCHIVO):
    st.error("❌ El archivo vehicles_us.csv no existe.")

    # Detiene la app aquí si falla la validación
    st.stop()


# CARGAR DATOS
car_data = pd.read_csv(ARCHIVO)


# VALIDAR COLUMNAS NECESARIAS
columnas_necesarias = ["odometer", "price"]

for col in columnas_necesarias:
    if col not in car_data.columns:
        st.error(f"❌ Falta la columna obligatoria: {col}")
        st.stop()


# MENSAJES DE VERIFICACIÓN DE CARGA
# Contenedor temporal para mensajes de carga
mensaje_carga = st.empty()

if not st.session_state.archivo_cargado:
    # mostrar mensaje de carga
    mensaje_carga.warning("⚠️ Cargando archivo vehicles_us.csv...")

    # Borrar mensaje de carga
    time.sleep(1)
    mensaje_carga.empty()

    # mostrar mensaje de éxito
    mensaje_carga.warning("✅ Archivo cargado correctamente.")

    # Borrar mensaje de éxito
    time.sleep(1)
    mensaje_carga.empty()

    # Marcar que ya se cargó el archivo
    st.session_state.archivo_cargado = True


# TÍTULO DE SECCIÓN DE FILTROS
st.subheader("🔎 Filtros de búsqueda")


# CÓDIGO PARA ELIMINAR OUTLIERS
# Crear checkbox para eliminar outliers
outliers_checkbox = st.checkbox(
    'Eliminar valores atípicos en el precio', value=True)

# Al hacer click en el checkbox de outliers
if outliers_checkbox:
    # Calcular IQR y límiteS
    Q1 = car_data["price"].quantile(0.25)
    Q3 = car_data["price"].quantile(0.75)
    IQR = Q3 - Q1

    limite_superior = Q3 + 1.5 * IQR

    car_data = car_data[car_data["price"] <= limite_superior]


# FILTROS INTERACTIVOS DE DATOS
# Eliminar valores nulos para evitar errores en sliders
car_data = car_data.dropna(subset=["price", "odometer"])

# Rango dinámico de precios
precio_min = int(car_data["price"].min())
precio_max = int(car_data["price"].max())

# Slider de rango de precios
precio_rango = st.slider(
    "💰 Rango de precios",
    min_value=precio_min,
    max_value=precio_max,
    value=(precio_min, precio_max)
)

# Rango dinámico de kilometraje
km_min = int(car_data["odometer"].quantile(0.01))
km_max = int(car_data["odometer"].quantile(0.99))

# Slider de rango de kilometraje
km_rango = st.slider(
    "🚗 Rango de kilometraje",
    min_value=km_min,
    max_value=km_max,
    value=(km_min, km_max)
)

# Aplicar filtros a los datos
filtered_data = car_data[
    (car_data["price"] >= precio_rango[0]) &
    (car_data["price"] <= precio_rango[1]) &
    (car_data["odometer"] >= km_rango[0]) &
    (car_data["odometer"] <= km_rango[1])
]

# Mostrar cuántos registros quedaron
st.info(
    f"📊 Número de registros después del filtrado: {filtered_data.shape[0]}")


# HISTOGRAMA
# crear un checkbox de histograma
hist_checkbox = st.checkbox('Construir histograma')

# al hacer clic en el checkbox de histograma
if hist_checkbox:
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de autos'
    )

    # crear un histograma
    fig = px.histogram(
        filtered_data,
        x="odometer",
        title="Distribución del kilometraje",
        labels={
            "odometer": "Odómetro (millas)"
        },
        opacity=0.7,
        nbins=60
    )
    fig.update_layout(yaxis_title="Cantidad de vehículos")
    fig.update_traces(marker_line_color="white", marker_line_width=0.5)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# GRÁFICO DE DISPERSIÓN
# crear un checkbox de grafico de dispersión
disp_checkbox = st.checkbox('Construir gráfico de dispersión')

# al hacer clic en el checkbox de gráfico de dispersión
if disp_checkbox:
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos '
        'de anuncios de venta de autos'
    )

    # crear un gráfico de dispersión
    fig = px.scatter(
        filtered_data,
        x="odometer",
        y="price",
        title="Relación entre el kilometraje y el precio del vehículo",
        labels={
            "odometer": "Odómetro (millas)",
            "price": "Precio (USD)"
        },
        opacity=0.5
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
