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
st.markdown("""
📉 **Why it matters today (2025):**
- Over **4.2 million children** remain undiagnosed globally.
- **82%** of undiagnosed cases are in countries without universal screening.
- NeuroConnect proposes a **cost-effective model**: $2,500 per child vs. $1.2M for lifelong ABA therapy.
- In 2025, for every 1 child diagnosed in the U.S., **12 remain invisible in Africa**.

#### **Country-Specific Data Highlights:**
- 🇺🇸 **USA**: 9,000 kits distributed; ~120,000 undiagnosed children despite a diagnostic rate of 1 in 36 (CDC, 2023).
- 🇰🇪 **Kenya**: 500 kits; 98,000 estimated undiagnosed due to limited infrastructure (WHO Africa, 2022).
- 🇳🇬 **Nigeria**: Only 250 kits; over 1 million undiagnosed — <10% access to diagnostic services (UNICEF, 2023).
- 🇵🇪 **Peru**: 450 kits; ~300,000 children estimated undiagnosed, especially in the Amazon region.
- 🇮🇳 **India**: 1,300 kits; over 1.4 million undiagnosed due to rural/urban disparity and clinician shortages.
""")

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
