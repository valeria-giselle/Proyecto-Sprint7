import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar la base de datos
data = pd.read_csv('./vehicles_us.csv')

# Configurar la aplicación
st.title("Aplicación Interactiva de Vehículos")
st.header("Explora los datos de vehículos en venta en U.S.A.")

# Crear un gráfico interactivo
st.subheader("Gráfico de Dispersión Interactivo")
scatter_fig = px.scatter(data, x='price', y='odometer', title='Precio vs Kilometraje', 
                          labels={'price': 'Precio', 'odometer': 'Kilometraje'}, 
                          hover_data=['model', 'model_year'])
st.plotly_chart(scatter_fig, use_container_width=True)

# Histograma generado por un botón
st.subheader("Genera el Histograma")
if st.button("Crear Histograma"):
    hist_fig = px.histogram(data, x='price', title='Distribución de Precios', labels={'price': 'Precio'})
    st.plotly_chart(hist_fig, use_container_width=True)
    st.success("¡Histograma generado!")
else:
    st.info("Haz clic en el botón para generar el histograma.")