import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Comparativa Técnica - ASISA",
    page_icon="📈",
    layout="wide"
)

# Colores
COLOR_POWERBI = '#F2C811'
COLOR_PROPUESTA = '#3ECF8E'
COLOR_NEGATIVO = '#E74C3C'
COLOR_POSITIVO = '#2ECC71'

st.title("📈 Comparativa Técnica: Power BI vs Streamlit + Supabase")
st.markdown("---")

# Introducción
st.markdown("""
Esta sección presenta un análisis comparativo técnico y económico entre las dos alternativas
para el desarrollo del Dashboard de ASISA.
""")

# Tabs para organizar
tab1, tab2, tab3, tab4 = st.tabs(["💰 Costes", "⚡ Rendimiento", "🔒 Seguridad", "📊 ROI"])

with tab1:
    st.subheader("💰 Comparativa de Costes Anuales")

    col1, col2 = st.columns([2, 1])

    with col1:
        categorias = ['Power BI Pro\n+ Azure SQL', 'Power BI Premium\n+ Azure SQL',
                      'Streamlit\n+ Supabase']
        costes = [22260, 52644, 960]
        colores = [COLOR_POWERBI, COLOR_POWERBI, COLOR_PROPUESTA]

        fig = go.Figure(data=[
            go.Bar(
                x=categorias,
                y=costes,
                text=[f'€{c:,}' for c in costes],
                textposition='auto',
                marker_color=colores,
                hovertemplate='<b>%{x}</b><br>Coste anual: €%{y:,}<extra></extra>'
            )
        ])

        fig.update_layout(
            yaxis_title='Coste Anual (€)',
            xaxis_title='Solución',
            showlegend=False,
            height=500,
            plot_bgcolor='white',
            yaxis=dict(gridcolor='lightgray')
        )

        fig.add_annotation(
            x=2, y=960,
            text=f"Ahorro: €21,300 - €51,684/año<br>(96-98% menos coste)",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor=COLOR_POSITIVO,
            ax=-150,
            ay=-80,
            bgcolor=COLOR_POSITIVO,
            font=dict(color='white', size=12),
            bordercolor=COLOR_POSITIVO,
            borderwidth=2
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.metric("Ahorro Anual", "€21,300 - €51,684", delta="96-98% menos")
        st.markdown("### Desglose Streamlit + Supabase")
        st.markdown("""
        - **Streamlit Cloud:** €0 (gratis)
        - **Supabase Pro:** €25/mes
        - **Total anual:** €300

        ### Escalabilidad
        - Usuarios ilimitados
        - Sin licencias adicionales
        - Hosting incluido
        """)

with tab2:
    st.subheader("⚡ Comparativa de Rendimiento")

    soluciones = ['Acceso\nDirecto', 'Power BI\nDirectQuery', 'Power BI\nImport Mode',
                  'Streamlit +\nSupabase']
    tiempos = [9.4, 9.4, 0.37, 0.2]
    colores = [COLOR_NEGATIVO, COLOR_POWERBI, COLOR_POWERBI, COLOR_PROPUESTA]

    fig = go.Figure(data=[
        go.Bar(
            x=soluciones,
            y=tiempos,
            text=[f'{t}s' for t in tiempos],
            textposition='auto',
            marker_color=colores,
            hovertemplate='<b>%{x}</b><br>Tiempo carga: %{y}s<extra></extra>'
        )
    ])

    fig.update_layout(
        yaxis_title='Tiempo de Carga (segundos)',
        xaxis_title='Solución',
        showlegend=False,
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='lightgray')
    )

    st.plotly_chart(fig, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Streamlit + Supabase", "0.2s", delta="-9.2s vs Acceso Directo")
    with col2:
        st.metric("Vs Power BI DirectQuery", "47x más rápido", delta_color="normal")
    with col3:
        st.metric("Vs Power BI Import", "1.85x más rápido", delta_color="normal")

with tab3:
    st.subheader("🔒 Comparativa de Seguridad")

    caracteristicas = [
        'Autenticación MFA',
        'Row Level Security',
        'Encriptación end-to-end',
        'Auditoría de accesos',
        'Backup automático',
        'GDPR compliant',
        'Control de permisos granular',
        'API segura (HTTPS)'
    ]

    powerbi = [1, 1, 1, 1, 1, 1, 1, 1]
    propuesta = [1, 1, 1, 1, 1, 1, 1, 1]

    df_security = pd.DataFrame({
        'Característica': caracteristicas,
        'Power BI Premium': powerbi,
        'Streamlit + Supabase': propuesta
    })

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Power BI Premium")
        for feat in caracteristicas:
            st.markdown(f"- ✅ {feat}")

    with col2:
        st.markdown("### ✅ Streamlit + Supabase")
        for feat in caracteristicas:
            st.markdown(f"- ✅ {feat}")

    st.success("**Ambas soluciones cumplen con los estándares de seguridad empresarial**")

with tab4:
    st.subheader("📊 Retorno de Inversión (ROI)")

    periodos = ['Año 1', 'Año 2', 'Año 3', 'Año 5']
    ahorro_pro = [21300, 42600, 63900, 106500]
    ahorro_premium = [51684, 103368, 155052, 258420]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Ahorro vs Power BI Pro',
        x=periodos,
        y=ahorro_pro,
        marker_color=COLOR_POSITIVO,
        text=[f'€{a:,}' for a in ahorro_pro],
        textposition='auto'
    ))

    fig.add_trace(go.Bar(
        name='Ahorro vs Power BI Premium',
        x=periodos,
        y=ahorro_premium,
        marker_color=COLOR_PROPUESTA,
        text=[f'€{a:,}' for a in ahorro_premium],
        textposition='auto'
    ))

    fig.update_layout(
        title='Ahorro Acumulado en el Tiempo',
        yaxis_title='Ahorro Total (€)',
        xaxis_title='Período',
        barmode='group',
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='lightgray')
    )

    st.plotly_chart(fig, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Ahorro 3 años", "€63,900 - €155,052")
    with col2:
        st.metric("Ahorro 5 años", "€106,500 - €258,420")
    with col3:
        st.metric("ROI", "Inmediato", delta="Desde mes 1")

# Resumen ejecutivo
st.markdown("---")
st.markdown("## 📋 Resumen Ejecutivo")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ✅ Ventajas Técnicas")
    st.markdown("""
    - Desarrollo ágil
    - Personalización total
    - Stack independiente
    - Integración directa con Supabase
    - Actualizaciones en tiempo real
    """)

with col2:
    st.markdown("### 💰 Ventajas Económicas")
    st.markdown("""
    - 96-98% menos coste
    - Sin licencias por usuario
    - Escalabilidad gratuita
    - ROI inmediato
    - Ahorro €100k+ en 5 años
    """)

with col3:
    st.markdown("### 🚀 Ventajas Operativas")
    st.markdown("""
    - Despliegue en minutos
    - Cambios instantáneos
    - Sin dependencia de proveedores
    - Mantenimiento simplificado
    - Equipo puede iterar rápido
    """)
