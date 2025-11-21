import streamlit as st
import os

st.set_page_config(
    page_title="Documentos Ejecutivos - ASISA",
    page_icon="📑",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .download-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        margin: 20px 0;
        text-align: center;
        color: white;
    }
    .download-box h2 {
        color: white;
        margin-bottom: 10px;
    }
    .download-box p {
        color: #f0f0f0;
        margin-bottom: 20px;
    }
    .highlight-box {
        background: #f8f9fa;
        border-left: 5px solid #667eea;
        padding: 20px;
        margin: 15px 0;
        border-radius: 5px;
    }
    .metric-card {
        background: white;
        border: 2px solid #667eea;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        color: #667eea;
        margin: 10px 0;
    }
    .metric-label {
        font-size: 14px;
        color: #666;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📑 Documentos Ejecutivos para CEO")
st.markdown("---")

# Banner informativo
st.markdown("""
    <div class='download-box'>
        <h2>🎯 Documentación Completa de la Propuesta</h2>
        <p>Descarga los documentos ejecutivos y técnicos para evaluar la implementación del Dashboard ASISA con Python + Streamlit + Supabase</p>
    </div>
""", unsafe_allow_html=True)

# Métricas destacadas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>Ahorro Anual</div>
            <div class='metric-value'>€21k-€52k</div>
            <div class='metric-label'>vs Power BI</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>ROI</div>
            <div class='metric-value'>+12%</div>
            <div class='metric-label'>Primer Año</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>Rendimiento</div>
            <div class='metric-value'>47x</div>
            <div class='metric-label'>Más Rápido</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>Disponibilidad</div>
            <div class='metric-value'>99.9%</div>
            <div class='metric-label'>Uptime SLA</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Sección de descargas
st.markdown("## 📥 Documentos Disponibles")

tab1, tab2, tab3 = st.tabs(["📄 Resumen Ejecutivo", "📊 Presentación Técnica", "📈 Gráficos Comparativos"])

with tab1:
    st.markdown("### 📄 Resumen Ejecutivo")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class='highlight-box'>
        <h4>¿Qué incluye este documento?</h4>
        <ul>
            <li>💰 <strong>Impacto económico</strong>: Ahorro de €21k-€52k anuales vs Power BI</li>
            <li>⚡ <strong>Ventajas técnicas</strong>: 47x más rápido, 99.9% disponibilidad</li>
            <li>🔒 <strong>Análisis de seguridad</strong>: Certificaciones ISO 27001, SOC 2</li>
            <li>📊 <strong>Comparativa detallada</strong>: PowerBI vs Streamlit+Supabase</li>
            <li>🚀 <strong>Plan de implementación</strong>: 7 semanas, 4 fases</li>
            <li>⚠️ <strong>Riesgos identificados</strong>: Dependencia Python, formación equipo</li>
            <li>✅ <strong>Recomendación final</strong>: Proceder con la solución propuesta</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        # Leer el contenido del archivo
        try:
            with open("resumen_ejecutivo_asisa.md", "r", encoding="utf-8") as f:
                resumen_content = f.read()

            st.download_button(
                label="⬇️ Descargar Resumen Ejecutivo (Markdown)",
                data=resumen_content,
                file_name="resumen_ejecutivo_asisa.md",
                mime="text/markdown",
                use_container_width=True
            )

            # Mostrar preview
            with st.expander("👁️ Ver Preview del Documento"):
                st.markdown(resumen_content)
        except FileNotFoundError:
            st.error("⚠️ Archivo no encontrado. Asegúrate de que 'resumen_ejecutivo_asisa.md' esté en el directorio raíz.")

    with col2:
        st.info("""
        **📋 Ideal para:**
        - CEO / Dirección General
        - CFO / Finanzas
        - CTO / IT

        **⏱️ Lectura:** 5-7 minutos

        **📊 Formato:** Markdown
        """)

with tab2:
    st.markdown("### 📊 Presentación Técnica Completa")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class='highlight-box'>
        <h4>¿Qué incluye este documento?</h4>
        <ul>
            <li>🏗️ <strong>Arquitectura del sistema</strong>: Diagramas detallados</li>
            <li>🔧 <strong>Stack tecnológico</strong>: Python, Streamlit, Supabase, Plotly</li>
            <li>📈 <strong>Análisis de rendimiento</strong>: Benchmarks y comparativas</li>
            <li>🔐 <strong>Seguridad y compliance</strong>: GDPR, ISO 27001, SOC 2</li>
            <li>💾 <strong>Estrategia ETL</strong>: Migración desde Access</li>
            <li>📊 <strong>KPIs y métricas</strong>: NS, TMO, TMA, conversión</li>
            <li>🗓️ <strong>Timeline de implementación</strong>: Desglose por fases</li>
            <li>💰 <strong>Análisis coste-beneficio</strong>: Comparativas detalladas</li>
            <li>🎯 <strong>Casos de uso</strong>: Escenarios de aplicación</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        try:
            with open("presentacion_tecnica_asisa.md", "r", encoding="utf-8") as f:
                presentacion_content = f.read()

            st.download_button(
                label="⬇️ Descargar Presentación Técnica (Markdown)",
                data=presentacion_content,
                file_name="presentacion_tecnica_asisa.md",
                mime="text/markdown",
                use_container_width=True
            )

            with st.expander("👁️ Ver Preview del Documento"):
                st.markdown(presentacion_content)
        except FileNotFoundError:
            st.error("⚠️ Archivo no encontrado. Asegúrate de que 'presentacion_tecnica_asisa.md' esté en el directorio raíz.")

    with col2:
        st.info("""
        **📋 Ideal para:**
        - Equipo técnico
        - Arquitectos de software
        - Product Managers
        - DevOps

        **⏱️ Lectura:** 15-20 minutos

        **📊 Formato:** Markdown
        """)

with tab3:
    st.markdown("### 📈 Gráficos Comparativos Interactivos")

    st.markdown("""
    <div class='highlight-box'>
    <h4>Visualizaciones Disponibles</h4>
    <p>Los siguientes gráficos HTML interactivos fueron generados con el script <code>generar_graficos_presentacion.py</code>:</p>
    </div>
    """, unsafe_allow_html=True)

    # Lista de gráficos
    graficos = {
        "grafico_1_costes.html": {
            "titulo": "💰 Comparativa de Costes Anuales",
            "desc": "Análisis económico: Power BI Pro vs Premium vs Streamlit+Supabase"
        },
        "grafico_2_rendimiento.html": {
            "titulo": "⚡ Comparativa de Rendimiento",
            "desc": "Tiempo de carga del dashboard en diferentes soluciones"
        },
        "grafico_3_disponibilidad.html": {
            "titulo": "🔄 Análisis de Disponibilidad",
            "desc": "Uptime y confiabilidad de cada solución"
        },
        "grafico_4_impacto_sistemas.html": {
            "titulo": "🖥️ Impacto en Sistemas Productivos",
            "desc": "Reducción de carga en TUIO, ARTEMISA y CORE SENDA"
        },
        "grafico_5_seguridad.html": {
            "titulo": "🔒 Comparativa de Seguridad",
            "desc": "Certificaciones, compliance y características de seguridad"
        },
        "grafico_6_timeline.html": {
            "titulo": "📅 Timeline de Implementación",
            "desc": "Planificación temporal de las 4 fases del proyecto"
        },
        "grafico_7_roi.html": {
            "titulo": "📊 Análisis de ROI",
            "desc": "Retorno de inversión proyectado a 5 años"
        },
        "grafico_8_matriz_decision.html": {
            "titulo": "🎯 Matriz de Decisión",
            "desc": "Evaluación ponderada de criterios técnicos y económicos"
        },
        "grafico_9_infografia_resumen.html": {
            "titulo": "📋 Infografía Resumen",
            "desc": "Síntesis visual de la propuesta completa"
        }
    }

    # Mostrar gráficos disponibles
    col1, col2, col3 = st.columns(3)

    for idx, (filename, info) in enumerate(graficos.items()):
        with [col1, col2, col3][idx % 3]:
            with st.container():
                st.markdown(f"**{info['titulo']}**")
                st.caption(info['desc'])

                if os.path.exists(filename):
                    with open(filename, "r", encoding="utf-8") as f:
                        html_content = f.read()

                    st.download_button(
                        label=f"⬇️ Descargar",
                        data=html_content,
                        file_name=filename,
                        mime="text/html",
                        key=f"btn_{filename}",
                        use_container_width=True
                    )
                else:
                    st.warning("⚠️ Archivo no disponible")

    st.markdown("<br>", unsafe_allow_html=True)

    # Botón para descargar el script generador
    st.markdown("#### 🔧 Script Generador de Gráficos")

    try:
        with open("generar_graficos_presentacion.py", "r", encoding="utf-8") as f:
            script_content = f.read()

        st.download_button(
            label="⬇️ Descargar Script Python (generar_graficos_presentacion.py)",
            data=script_content,
            file_name="generar_graficos_presentacion.py",
            mime="text/x-python",
            use_container_width=True
        )

        st.info("""
        **💡 Nota:** Este script Python genera todos los gráficos HTML interactivos.
        Puedes ejecutarlo localmente con: `python generar_graficos_presentacion.py`
        """)
    except FileNotFoundError:
        st.error("⚠️ Script no encontrado.")

st.markdown("---")

# Resumen final
st.markdown("## 🎯 Resumen Ejecutivo Rápido")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ✅ Por qué elegir Streamlit + Supabase

    1. **Ahorro significativo:** €21k-€52k/año vs Power BI
    2. **Rendimiento superior:** 47x más rápido que acceso directo
    3. **Sin licencias por usuario:** Escalabilidad ilimitada
    4. **Control total:** Código abierto, sin vendor lock-in
    5. **Desarrollo ágil:** Actualizaciones en minutos
    6. **Seguridad empresarial:** ISO 27001, SOC 2, GDPR
    7. **Protege sistemas productivos:** 99.96% menos queries
    """)

with col2:
    st.markdown("""
    ### 📊 Comparativa Rápida

    | Característica | Power BI | Streamlit |
    |---|---|---|
    | **Coste anual** | €22k-€53k | €960 |
    | **Licencias** | Por usuario | Ilimitadas |
    | **Carga** | 0.37-9.4s | 0.2s |
    | **Personalización** | Limitada | Total |
    | **Vendor lock-in** | Sí | No |
    | **Hosting** | Extra | Gratis |
    """)

st.markdown("---")

# Call to action
st.success("""
### 🚀 Próximos Pasos

1. **Revisar** los documentos descargados
2. **Evaluar** la comparativa técnica y económica
3. **Decidir** sobre la tecnología a utilizar
4. **Planificar** la implementación (7 semanas, 4 fases)

**¿Preguntas?** Contacta con el equipo técnico para una demo detallada o aclaraciones.
""")
