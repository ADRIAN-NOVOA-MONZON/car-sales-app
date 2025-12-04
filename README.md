# car-sales-app
Análisis Exploratorio de Datos – Ventas de Vehículos

Aplicación web interactiva desarrollada con Streamlit para realizar análisis exploratorio de datos (EDA) sobre vehículos en venta. Permite analizar el comportamiento del kilometraje y su relación con el precio mediante visualizaciones dinámicas.

# 🌐 Aplicación Web en Vivo
Ver aplicación desplegada [aquí](https://car-sales-app-wag5.onrender.com/)

# 🛠️ Tecnologías Utilizadas
• Python<br>
• Pandas<br>
• Streamlit<br>
• Plotly Express<br>

# 📊 Funcionalidades
• Histograma interactivo del kilometraje<br>
• Gráfico de dispersión entre precio y odómetro<br>
• Interfaz dinámica con checkboxes<br>
• Visualizaciones interactivas<br>

# ⚙️ Instalación local
git clone https://github.com/ADRIAN-NOVOA-MONZON/car-sales-app.git <br>
cd car-sales-app<br>
python -m venv venv<br>
venv\Scripts\activate<br>
pip install -r requirements.txt<br>

# ▶️ Ejecución
streamlit run app.py

# 🗃️ Dataset
El archivo vehicles_us.csv contiene información de venta de autos, los cuales corresponden a lo siguiente:<br>
• price – Precio del vehículo<br>
• model_year – Año del modelo<br>
• model – Modelo del vehículo<br>
• condition – Condición del vehículo (nuevo, usado, excelente, etc.)<br>
• cylinders – Número de cilindros<br>
• fuel – Tipo de combustible<br>
• odometer – Kilometraje del vehículo<br>
• transmission – Tipo de transmisión (automática o manual)<br>
• type – Tipo de vehículo (sedán, SUV, pickup, etc.)<br>
• paint_color – Color del vehículo<br>
• is_4wd – Indica si cuenta con tracción en las cuatro ruedas (4WD)<br>
• date_posted – Fecha de publicación del vehículo<br>
• days_listed – Días que el vehículo estuvo publicado<br>

# 👨‍💻 Autor
Adrian Novoa Monzón<br>
Data Analyst en Formación – TripleTen