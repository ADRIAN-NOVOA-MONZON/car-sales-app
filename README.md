# car-sales-app
Análisis Exploratorio de Datos – Ventas de Vehículos

Aplicación web interactiva desarrollada con Streamlit para realizar análisis exploratorio de datos (EDA) sobre vehículos en venta. Permite analizar el comportamiento del kilometraje y su relación con el precio mediante visualizaciones dinámicas.

🛠️ Tecnologías Utilizadas
• Python 3
• Pandas
• Streamlit
• Plotly Express

📊 Funcionalidades
• Histograma interactivo del kilometraje
• Gráfico de dispersión entre precio y odómetro
• Interfaz dinámica con checkboxes
• Visualizaciones interactivas

⚙️ Instalación
git clone https://github.com/ADRIAN-NOVOA-MONZON/car-sales-app.git
cd car-sales-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

▶️ Ejecución
streamlit run app.py

🗃️ Dataset
El archivo vehicles_us.csv contiene información de venta de autos, los cuales corresponden a lo siguiente:
price – Precio del vehículo
model_year – Año del modelo
model – Modelo del vehículo
condition – Condición del vehículo (nuevo, usado, excelente, etc.)
cylinders – Número de cilindros
fuel – Tipo de combustible
odometer – Kilometraje del vehículo
transmission – Tipo de transmisión (automática o manual)
type – Tipo de vehículo (sedán, SUV, pickup, etc.)
paint_color – Color del vehículo
is_4wd – Indica si cuenta con tracción en las cuatro ruedas (4WD)
date_posted – Fecha de publicación del vehículo
days_listed – Días que el vehículo estuvo publicado

👨‍💻 Autor
Adrian Novoa Monzón
Data Analyst en Formación – TripleTen