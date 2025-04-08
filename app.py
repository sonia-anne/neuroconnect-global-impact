# NEUROCONNECT: Cost-Scalability Dashboard — APP.PY COMPLETO Y ACTUALIZADO

# Imports
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile
import os

# CONFIGURACIÓN GENERAL
st.set_page_config(page_title="NeuroConnect Global Impact Dashboard", layout="wide")

# MODO OSCURO TOTAL
st.markdown("""
<style>
body, .stApp {
    background-color: #0d1117;
    color: white;
}
h1, h2, h3, h4, h5, h6, p, span, div {
    color: white !important;
}
.plot-container {
    background-color: #0d1117 !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 NeuroConnect: Global Impact & Cost-Effectiveness Dashboard")

# =====================
# Comparación de Costos
# =====================
data = {
    "Treatment": ["NeuroConnect", "ABA Therapy", "Pharmacotherapy"],
    "Cost per Patient (USD)": [2500, 1200000, 12500],
    "Patients per 100K USD": [83, 1.6, 8],
    "Effectiveness (%)": [90, 35, 45]
}
df = pd.DataFrame(data)
fig = go.Figure()
fig.add_trace(go.Bar(x=df['Treatment'], y=df['Patients per 100K USD'], name='Patients per $100K'))
fig.add_trace(go.Bar(x=df['Treatment'], y=df['Effectiveness (%)'], name='Effectiveness (%)'))
fig.update_layout(
    title={"text": "🧠 Cost vs Effectiveness (per $100,000)", "font": {"color": "white"}},
    barmode='group',
    template='plotly_dark',
    paper_bgcolor='#0d1117',
    plot_bgcolor='#0d1117',
    font=dict(color='white')
)
st.plotly_chart(fig, use_container_width=True)

# =====================
# Mapa de Prevalencia
# =====================
st.subheader("📊 Autism Prevalence by Country")
country_data = pd.DataFrame({
    "Country": ["United States", "United Kingdom", "South Korea", "Ecuador", "Nigeria", "Bangladesh"],
    "Prevalence": [27.8, 20.0, 17.5, 2.0, 1.2, 1.0]  # per 1,000 children
})
fig_map = px.choropleth(
    country_data,
    locations="Country",
    locationmode="country names",
    color="Prevalence",
    color_continuous_scale="Viridis",
    title="🌍 Autism Prevalence per 1,000 Children",
    template='plotly_dark'
)
fig_map.update_layout(
    paper_bgcolor="#0d1117",
    plot_bgcolor="#0d1117",
    font=dict(color='white'),
    geo=dict(bgcolor='#0d1117')
)
st.plotly_chart(fig_map, use_container_width=True)

# ===========================
# Inequity bubble map
# ===========================
st.subheader("🌐 Inequity in Diagnosis Access")
bubble_df = pd.DataFrame({
    "Country": ["Nigeria", "Peru", "India", "Ghana", "UK", "USA"],
    "Undiagnosed": [950000, 320000, 1500000, 500000, 45000, 70000],
    "Access": ["No", "No", "Partial", "No", "Yes", "Yes"],
    "lat": [9.082, -9.19, 20.59, 7.9465, 55.3781, 37.0902],
    "lon": [8.6753, -75.0152, 78.96, -1.0232, -3.4360, -95.7129]
})
fig_bubble = px.scatter_geo(
    bubble_df,
    lat="lat",
    lon="lon",
    size="Undiagnosed",
    color="Access",
    hover_name="Country",
    title="🔴 Undiagnosed Children + NeuroConnect Access",
    template='plotly_dark',
    projection="natural earth"
)
fig_bubble.update_layout(
    paper_bgcolor="#0d1117",
    plot_bgcolor="#0d1117",
    font=dict(color='white'),
    geo=dict(bgcolor='#0d1117')
)
st.plotly_chart(fig_bubble, use_container_width=True)

# ===========================
# Gráfico de Radar Accesibilidad
# ===========================
st.subheader("📡 Accessibility to Autism Care: USA vs Nigeria")
radar = pd.DataFrame({
    'Factor': ['Diagnostics', 'Therapy Innovation', 'Trained Staff', 'Infrastructure', 'Funding'],
    'USA': [10, 9, 9, 10, 9],
    'Nigeria': [2, 1, 2, 3, 2]
})
fig_radar = go.Figure()
for country in ['USA', 'Nigeria']:
    fig_radar.add_trace(go.Scatterpolar(
        r=radar[country],
        theta=radar['Factor'],
        fill='toself',
        name=country
    ))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0,10])),
    title={"text": "🛰️ Equity in Autism Diagnosis & Treatment", "font": {"color": "white"}},
    template='plotly_dark',
    paper_bgcolor='#0d1117',
    font=dict(color='white')
)
st.plotly_chart(fig_radar, use_container_width=True)

# ===========================
# Mensaje Final
# ===========================
st.markdown("""
✅ **Conclusion:**  
> NeuroConnect is not just frontier science. It's global medical justice.

**Data Sources:**  
- CDC (2023)  
- NHS (2022)  
- OMS (2022)  
- UNICEF (2024)
""")
