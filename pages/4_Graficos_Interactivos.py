import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Gráficos Interactivos - ASISA",
    page_icon="📊",
    layout="wide"
)

# Verificar autenticación
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("⚠️ Por favor, inicia sesión desde la página principal")
    st.stop()

st.title("📊 Gráficos Interactivos - Análisis Comparativo")
st.markdown("---")

st.markdown("""
Estos gráficos interactivos muestran el análisis completo de la propuesta **Streamlit + Supabase vs Power BI**.
Puedes hacer zoom, pasar el ratón para ver detalles, y explorar los datos de forma interactiva.
""")

# Lista de gráficos con sus descripciones
graficos = {
    "grafico_1_costes.html": {
        "titulo": "💰 Comparativa de Costes Anuales",
        "desc": "Análisis económico detallado: Power BI Pro vs Premium vs Streamlit+Supabase. **Ahorro de €21k-€52k/año**"
    },
    "grafico_2_rendimiento.html": {
        "titulo": "⚡ Comparativa de Rendimiento",
        "desc": "Tiempo de carga del dashboard. **Streamlit es 47x más rápido** que acceso directo"
    },
    "grafico_3_disponibilidad.html": {
        "titulo": "🔄 Análisis de Disponibilidad",
        "desc": "Uptime y confiabilidad. **99.9% disponibilidad** con Streamlit+Supabase"
    },
    "grafico_4_impacto_sistemas.html": {
        "titulo": "🖥️ Impacto en Sistemas Productivos",
        "desc": "Reducción de carga en TUIO, ARTEMISA y CORE SENDA. **99.96% menos queries**"
    },
    "grafico_5_seguridad.html": {
        "titulo": "🔒 Comparativa de Seguridad",
        "desc": "Certificaciones ISO 27001, SOC 2, GDPR compliance y características de seguridad"
    },
    "grafico_6_timeline.html": {
        "titulo": "📅 Timeline de Implementación",
        "desc": "Planificación temporal de las 4 fases del proyecto. **7 semanas** de desarrollo"
    },
    "grafico_7_roi.html": {
        "titulo": "📊 Análisis de ROI",
        "desc": "Retorno de inversión proyectado. **ROI +12% en año 1**, €100k+ ahorro en 5 años"
    },
    "grafico_8_matriz_decision.html": {
        "titulo": "🎯 Matriz de Decisión",
        "desc": "Evaluación ponderada de criterios técnicos y económicos comparando ambas soluciones"
    },
    "grafico_9_infografia_resumen.html": {
        "titulo": "📋 Infografía Resumen",
        "desc": "Síntesis visual completa de la propuesta con todos los KPIs principales"
    }
}

# Crear tabs para cada gráfico
tab_names = [info["titulo"] for info in graficos.values()]
tabs = st.tabs(tab_names)

for idx, (filename, info) in enumerate(graficos.items()):
    with tabs[idx]:
        st.markdown(f"### {info['titulo']}")
        st.markdown(info['desc'])
        st.markdown("---")

        # Intentar cargar y mostrar el gráfico HTML
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    html_content = f.read()

                # Mostrar el gráfico HTML embebido
                components.html(html_content, height=600, scrolling=True)

                # Botón de descarga
                st.download_button(
                    label=f"⬇️ Descargar {filename}",
                    data=html_content,
                    file_name=filename,
                    mime="text/html",
                    key=f"download_{filename}"
                )

            except Exception as e:
                st.error(f"⚠️ Error al cargar el gráfico: {str(e)}")
        else:
            st.warning(f"⚠️ Archivo {filename} no encontrado")
            st.info("""
            **Para generar los gráficos localmente:**

            ```bash
            python generar_graficos_presentacion.py
            ```

            Los gráficos se generarán en el directorio raíz del proyecto.
            """)

st.markdown("---")

# Resumen de insights
st.markdown("## 🎯 Insights Clave de los Gráficos")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 💰 Económico
    - **€21k-€52k ahorro/año**
    - 96-98% reducción de costes
    - ROI +12% primer año
    - Break-even en mes 11
    """)

with col2:
    st.markdown("""
    ### ⚡ Técnico
    - **47x más rápido** que acceso directo
    - 99.9% disponibilidad
    - 99.96% menos carga en sistemas
    - 0.2s tiempo de carga
    """)

with col3:
    st.markdown("""
    ### 🔒 Seguridad
    - ISO 27001 + SOC 2
    - GDPR compliant
    - Row Level Security
    - Backups automáticos
    """)

st.success("""
### ✅ Recomendación

Basado en el análisis completo de estos gráficos, la solución **Streamlit + Supabase** ofrece:
- **Mejor rendimiento** técnico
- **Menores costes** operativos
- **Igual o mejor seguridad**
- **Mayor flexibilidad** de desarrollo

**Conclusión:** Proceder con la implementación de Streamlit + Supabase para el dashboard de ASISA.
""")
