import streamlit as st

st.set_page_config(
    page_title="Documentación - ASISA",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Documentación Técnica")
st.markdown("---")

# Introducción
st.markdown("""
# Dashboard Call Center ASISA

Dashboard interactivo para visualización de KPIs del Call Center de ASISA, desarrollado con Python y Streamlit.
Este documento detalla la arquitectura técnica, características y propuesta de implementación.
""")

# Características actuales
st.markdown("## 🎯 Características del Prototipo")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Visualización de Métricas
    - **Nivel de Servicio (NS):** Objetivo 90%
    - **Volumen de llamadas:** Total y atendidas
    - **TMO:** Tiempo Medio Operativo
    - **TMA:** Tiempo Medio de Atención
    - **Tasa de Conversión:** Presupuestos vs Pólizas
    - **KPIs por agente:** Ranking y comparativas

    ### Filtros Dinámicos
    - Por vertical (Venta, Retención, Outbound, Inbound)
    - Por rango de fechas
    - Por agente (solo director/comercial)
    - Granularidad temporal (día, semana, mes)
    """)

with col2:
    st.markdown("""
    ### Funcionalidades Interactivas
    - Gráficos interactivos con Plotly
    - Visualizaciones estadísticas con Seaborn
    - Sistema de pestañas (Tendencias, Análisis, Agentes)
    - Exportación de datos a CSV
    - Tablas con formato condicional

    ### Autenticación
    - Login básico por rol
    - Permisos granulares por usuario
    - Sesión persistente
    """)

st.markdown("---")

# Stack Tecnológico
st.markdown("## 🛠️ Stack Tecnológico")

tab1, tab2, tab3 = st.tabs(["Frontend", "Backend", "Infraestructura"])

with tab1:
    st.markdown("""
    ### Frontend

    **Streamlit 1.51.0**
    - Framework Python para crear aplicaciones web interactivas
    - Componentes nativos para dashboards
    - Actualizaciones en tiempo real
    - Sin necesidad de HTML/CSS/JavaScript

    **Plotly 6.5.0**
    - Gráficos interactivos profesionales
    - Hover tooltips personalizables
    - Zoom, pan, exportación de imágenes
    - Rendimiento optimizado

    **Seaborn + Matplotlib**
    - Visualizaciones estadísticas avanzadas
    - Heatmaps, distribuciones, correlaciones
    - Personalización completa de estilos
    """)

with tab2:
    st.markdown("""
    ### Backend (Propuesto)

    **Supabase (PostgreSQL)**
    - Base de datos relacional en la nube
    - APIs REST automáticas
    - Row Level Security (RLS)
    - Realtime subscriptions
    - Autenticación integrada

    **Pandas 2.3.3**
    - Procesamiento de datos eficiente
    - Transformaciones y agregaciones
    - Integración con NumPy

    **ETL Pipeline**
    - Ingesta desde Acces actual
    - Transformación y limpieza
    - Carga incremental a Supabase
    - Programación con cron/Airflow
    """)

with tab3:
    st.markdown("""
    ### Infraestructura

    **Streamlit Cloud (Hosting)**
    - Despliegue automático desde GitHub
    - SSL/TLS incluido
    - CDN global
    - Escalado automático
    - **Coste: €0 (gratis)**

    **Supabase Cloud**
    - Plan Pro: €25/mes
    - 8GB base de datos
    - 100GB transferencia
    - Backups automáticos diarios
    - 99.9% uptime SLA

    **GitHub**
    - Control de versiones
    - CI/CD automático
    - Revisión de código
    - Historial completo
    """)

st.markdown("---")

# Propuesta de implementación
st.markdown("## 🚀 Propuesta de Implementación para ASISA")

st.markdown("""
### Fase 1: Migración de Datos (2 semanas)

**Objetivos:**
- Migrar datos de Access a Supabase PostgreSQL
- Configurar Row Level Security
- Crear vistas materializadas para KPIs

**Entregables:**
- Base de datos en Supabase operativa
- Scripts ETL programados
- Documentación de esquema

---

### Fase 2: Dashboard Principal (2 semanas)

**Objetivos:**
- Conectar Streamlit con Supabase real
- Implementar autenticación completa (email + MFA)
- Desplegar métricas principales con datos reales

**Entregables:**
- Dashboard funcional con datos reales
- Sistema de roles (director, comercial, agente)
- Filtros dinámicos operativos

---

### Fase 3: Funcionalidades Avanzadas (2 semanas)

**Objetivos:**
- Alertas automáticas (NS < 90%, etc.)
- Reportes programados por email
- Comparativas históricas
- Predicciones con ML (opcional)

**Entregables:**
- Sistema de alertas configurado
- Reportes automatizados
- Documentación de usuario

---

### Fase 4: Testing y Despliegue (1 semana)

**Objetivos:**
- Testing con usuarios reales
- Optimización de performance
- Capacitación del equipo

**Entregables:**
- Dashboard en producción
- Manual de usuario
- Equipo capacitado
""")

st.markdown("---")

# Arquitectura
st.markdown("## 🏗️ Arquitectura del Sistema")

st.markdown("""
```
┌─────────────────────────────────────────────────────────────┐
│                     USUARIOS (Navegador)                     │
│  Director │ Comercial │ Agente │ CEO                         │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTPS
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   STREAMLIT CLOUD                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Dashboard   │  │  Comparativa │  │ Documentación│      │
│  │     KPIs     │  │   Técnica    │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────────────────┬────────────────────────────────────┘
                         │ API REST
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    SUPABASE (Backend)                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         PostgreSQL Database                          │   │
│  │  • Tabla llamadas  • Tabla agentes                   │   │
│  │  • Tabla ventas    • Tabla usuarios                  │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Row Level Security (RLS)                            │   │
│  │  • Agentes solo ven sus datos                        │   │
│  │  • Directores ven todo                               │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Auth & Realtime                                     │   │
│  │  • Autenticación MFA                                 │   │
│  │  • Updates en tiempo real                            │   │
│  └──────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │ ETL Scheduled
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              ACCESS DATABASE (Sistema actual)                │
│  • Datos históricos                                          │
│  • Sincronización programada                                 │
└─────────────────────────────────────────────────────────────┘
```
""")

st.markdown("---")

# Comparativa
st.markdown("## ⚖️ Comparativa: Streamlit vs Power BI")

comparison_data = {
    "Característica": [
        "Coste anual (50 usuarios)",
        "Licencias por usuario",
        "Tiempo de desarrollo",
        "Personalización",
        "Integración con Supabase",
        "Actualizaciones",
        "Hosting",
        "Escalabilidad",
        "Dependencia vendor",
        "Curva de aprendizaje equipo"
    ],
    "Power BI Premium": [
        "€52,644",
        "Incluidas en Premium",
        "Medio-Alto",
        "Limitada",
        "Via ODBC",
        "Lentas (deploy manual)",
        "Azure (adicional)",
        "Costosa",
        "Microsoft",
        "Media-Alta"
    ],
    "Streamlit + Supabase": [
        "€300",
        "Ilimitadas",
        "Rápido",
        "Total",
        "Nativa",
        "Instantáneas (git push)",
        "Incluido gratis",
        "Gratuita",
        "Ninguna",
        "Baja (Python)"
    ]
}

st.table(comparison_data)

st.markdown("---")

# Instalación Local
st.markdown("## 💻 Instalación Local (Desarrolladores)")

st.code("""
# 1. Clonar repositorio
git clone https://github.com/MariaVictoriaCairos/Prueba-dashboard.git
cd Prueba-dashboard

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\\Scripts\\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar aplicación
streamlit run dashboard.py

# 5. Abrir navegador en http://localhost:8501
""", language="bash")

st.markdown("---")

# Credenciales demo
st.markdown("## 🔑 Credenciales de Demo")

st.info("""
**Usuario:** director
**Contraseña:** demo123

*Nota: En producción, esto se reemplazará con autenticación real vía Supabase Auth*
""")

st.markdown("---")

# Próximos pasos
st.markdown("## 📋 Próximos Pasos")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Para Demo
    - ✅ Prototipo funcional desplegado
    - ✅ Comparativa técnica disponible
    - ✅ Documentación completa
    - ⏳ Feedback del CEO
    - ⏳ Decisión de stack tecnológico
    """)

with col2:
    st.markdown("""
    ### Para Producción
    - ⏳ Migración Access → Supabase
    - ⏳ Autenticación real
    - ⏳ Datos reales de ASISA
    - ⏳ Testing con usuarios
    - ⏳ Go-live
    """)

st.markdown("---")

# Contacto
st.markdown("## 📬 Contacto y Soporte")

st.markdown("""
**Desarrollado por:** María Victoria Cairós
**Repositorio:** [github.com/MariaVictoriaCairos/Prueba-dashboard](https://github.com/MariaVictoriaCairos/Prueba-dashboard)
**Stack:** Python + Streamlit + Plotly + Seaborn + Supabase (propuesto)

Para preguntas técnicas o solicitudes de features, abrir un issue en GitHub.
""")
