# neuroconnect_dashboard/app.py

# (Todo el contenido anterior permanece igual...)

# =============================
# ✅ Módulo 9: Impacto Global y Accesibilidad
# =============================

st.subheader("🌍 Global Impact Map & Accessibility - NeuroConnect vs. Inequity")
st.markdown("""
Perfecto. Para esta sección clave de impacto social y equidad, vamos a construir un **módulo visual avanzado y científicamente sustentado** que evidencie las desigualdades actuales **y cómo NeuroConnect propone una solución real con su modelo “uno por uno”**.

---

### ✅ **Módulo 9: Mapa de Impacto Global y Accesibilidad**

#### 📌 Objetivo:
Visualizar la **disparidad global en diagnóstico y tratamiento del autismo**, y cómo NeuroConnect rompe esa brecha con un modelo ético y escalable.

---

### **🧠 Gráficos incluidos:**

#### 1. Choropleth Map: Autism Prevalence by Country
""")
# Choropleth map
country_data = pd.DataFrame({
    "Country": ["United States", "United Kingdom", "South Korea", "Ecuador", "Nigeria", "Bangladesh"],
    "Prevalence": [27.8, 20.0, 17.5, 2.0, 1.2, 1.0]  # per 1,000 children
})
fig_map = px.choropleth(
    country_data,
    locations="Country",
    locationmode="country names",
    color="Prevalence",
    color_continuous_scale="RdBu_r",
    title="🌍 Autism Prevalence per 1,000 Children (2023 data)",
    template='plotly_dark'
)
fig_map.update_layout(paper_bgcolor="#0d1117", font=dict(color='white'))
st.plotly_chart(fig_map, use_container_width=True)

# Bubble Map Placeholder: Will be replaced with real inequality stats
st.markdown("""
#### 2. Bubble Map of Diagnostic Inequity
- Red = High invisibility rate (undiagnosed children)
- Green = Coverage by NeuroConnect (proposed sites)
""")

inequity_df = pd.DataFrame({
    "Country": ["Nigeria", "Peru", "India", "Ghana", "UK", "USA"],
    "Undiagnosed": [950000, 320000, 1500000, 500000, 45000, 70000],
    "Access": ["No", "No", "Partial", "No", "Yes", "Yes"],
    "lat": [9.082, -9.19, 20.59, 7.9465, 55.3781, 37.0902],
    "lon": [8.6753, -75.0152, 78.96, -1.0232, -3.4360, -95.7129]
})
fig_bubble = px.scatter_geo(
    inequity_df,
    lat="lat",
    lon="lon",
    size="Undiagnosed",
    color="Access",
    hover_name="Country",
    title="🔴 Children with Autism Undiagnosed + NeuroConnect Access",
    template='plotly_dark',
    projection="natural earth"
)
fig_bubble.update_layout(paper_bgcolor="#0d1117", font=dict(color='white'))
st.plotly_chart(fig_bubble, use_container_width=True)

# Flowmap placeholder with connecting lines (simulado)
st.markdown("""
#### 3. Flowmap: “One for One” Solidarity Model
Each treated child in USA 🇺🇸 supports one in Ghana 🇬🇭, Bolivia 🇧🇴, or Nepal 🇳🇵
""")
flowmap_df = pd.DataFrame({
    "origin": ["USA", "UK"],
    "target": ["Ghana", "Nepal"],
    "lines": [1, 1],
})
fig_flow = go.Figure()
fig_flow.add_trace(go.Scattergeo(
    locationmode = 'country names',
    lon = [-95.71, -1.0232, -3.436, 84.1240],
    lat = [37.09, 7.9465, 55.378, 28.3949],
    text = ["USA", "Ghana", "UK", "Nepal"],
    mode = 'markers+text',
    textposition="bottom center",
    marker = dict(size = 10, color = "green")
))
fig_flow.update_layout(title="🌐 Global Solidarity Links (NeuroConnect '1 for 1')", geo=dict(showland=True),
                       paper_bgcolor="#0d1117", font=dict(color='white'))
st.plotly_chart(fig_flow, use_container_width=True)

# Radar: Accessibility vs Equity
st.markdown("""
#### 4. Radar Chart: Healthcare Accessibility Factors
Comparison of available diagnostic infrastructure and NeuroConnect rollout.
""")
radar_compare = pd.DataFrame({
    'Factor': ['Diagnostics', 'Therapy Innovation', 'Trained Staff', 'Infrastructure', 'Funding'],
    'USA': [10, 9, 9, 10, 9],
    'Nigeria': [2, 1, 2, 3, 2]
})
fig_radar = go.Figure()
for country in ['USA', 'Nigeria']:
    fig_radar.add_trace(go.Scatterpolar(
        r=radar_compare[country],
        theta=radar_compare['Factor'],
        fill='toself',
        name=country
    ))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0,10])),
    title={"text": "📡 Equity in Autism Diagnosis and Treatment", "font": {"color": "white"}},
    template='plotly_dark',
    paper_bgcolor='#0d1117',
    font=dict(color='white')
)
st.plotly_chart(fig_radar, use_container_width=True)

st.markdown("""
✅ **Mensaje final de esta sección:**  
> “NeuroConnect no es solo ciencia de frontera. Es justicia médica global.”
""")
