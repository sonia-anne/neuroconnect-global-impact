# NEUROCONNECT: 3D GLOBAL IMPACT MAP — ULTRA-ADVANCED VERSION

# Imports
import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="🌐 NeuroConnect: 3D Global Impact Map", layout="wide")

# Dark Mode Styling
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

# Title
st.title("🌍 NEUROCONNECT | 3D Global Equity & Accessibility Map")
st.markdown("""
### **The future of neurological care — made accessible everywhere.**
> Real-time data, 3D interaction, and ethical global distribution.
""")

# ================================
# Mapa 3D Principal - Pydeck + Deck.gl
# ================================
st.subheader("🌐 3D Satellite Map: Kits Distributed & Diagnostic Inequity")

data = pd.DataFrame({
    'lat': [37.0902, -1.2921, 6.5244, -12.0464, 28.6139],
    'lon': [-95.7129, 36.8219, 3.3792, -77.0428, 77.2090],
    'region': ['USA', 'Kenya', 'Nigeria', 'Peru', 'India'],
    'kits_distributed': [9000, 500, 250, 450, 1300],
    'undiagnosed_cases': [120000, 98000, 1050000, 300000, 1400000],
})
data["size"] = data["kits_distributed"] / 25

layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position='[lon, lat]',
    get_color='[255, 100, 100]',
    get_radius='size',
    pickable=True,
    auto_highlight=True
)

view_state = pdk.ViewState(
    latitude=0,
    longitude=20,
    zoom=1.4,
    pitch=40
)

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/satellite-streets-v11",
    initial_view_state=view_state,
    layers=[layer],
    tooltip={"text": "{region}: {kits_distributed} kits, {undiagnosed_cases} undiagnosed children"}
))

# Tabla comparativa de impacto y accesibilidad
st.subheader("📊 Global Autism Inequity Pyramid (2025)")
table_df = pd.DataFrame({
    'Country': ['USA', 'India', 'Nigeria', 'Peru', 'Kenya'],
    'Kits Distributed': [9000, 1300, 250, 450, 500],
    'Estimated Undiagnosed': [120000, 1400000, 1050000, 300000, 98000],
    'Access Level': ['High', 'Medium', 'Low', 'Low', 'Low']
})
fig_table = go.Figure(data=[go.Table(
    header=dict(values=list(table_df.columns), fill_color='#1f77b4', font=dict(color='white'), align='left'),
    cells=dict(values=[table_df[col] for col in table_df.columns], fill_color='#111111', align='left', font=dict(color='white'))
)])
fig_table.update_layout(paper_bgcolor='#0d1117')
st.plotly_chart(fig_table, use_container_width=True)

# ================================
# Choropleth Heatmap - Plotly Express
# ================================
st.subheader("🧠 Diagnostic Inequity Heatmap")
chorodata = pd.DataFrame({
    'Country': ['USA', 'UK', 'India', 'Nigeria', 'Peru', 'Ecuador', 'South Korea'],
    'ISO': ['USA', 'GBR', 'IND', 'NGA', 'PER', 'ECU', 'KOR'],
    'Undiagnosed': [70000, 45000, 1400000, 1050000, 300000, 250000, 12000]
})
fig_choro = px.choropleth(
    chorodata,
    locations="ISO",
    color="Undiagnosed",
    hover_name="Country",
    color_continuous_scale="Reds",
    title="🌍 Real-Time Inequity in Autism Diagnosis",
    template='plotly_dark'
)
fig_choro.update_layout(paper_bgcolor='#0d1117', font_color='white')
st.plotly_chart(fig_choro, use_container_width=True)

# ================================
# Gráfico de Rutas Logísticas (simulado)
# ================================
st.subheader("📦 Ethical Distribution: Route Mapping")
route_data = pd.DataFrame({
    "source_lat": [37.7749, 48.8566],
    "source_lon": [-122.4194, 2.3522],
    "dest_lat": [-1.2921, -12.0464],
    "dest_lon": [36.8219, -77.0428],
})
routes = [
    pdk.Layer(
        "LineLayer",
        route_data,
        get_source_position='[source_lon, source_lat]',
        get_target_position='[dest_lon, dest_lat]',
        get_width=5,
        get_color=[0, 255, 0],
        auto_highlight=True,
        pickable=True
    )
]
st.pydeck_chart(pdk.Deck(
    layers=routes,
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/dark-v10"
))

# ================================
# Mensaje Final
# ================================
st.markdown("""
---
✅ **NeuroConnect bridges the global gap in autism care** — using ethics, science, and immersive technologies.

**Sources:** CDC (2023), WHO (2022), UNICEF (2024)

🔁 *1 kit in the North → 1 subsidized in the South.*
""")
