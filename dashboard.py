# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# ========================================
# CONFIGURACIÓN DE LA PÁGINA
# ========================================
st.set_page_config(
    page_title="ASISA - Dashboard KPIs",
    page_icon="📊",
    layout="wide"  # Pantalla completa
)

# ========================================
# AUTENTICACIÓN BÁSICA (después mejoraremos)
# ========================================
def check_login():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        st.title("🔐 Login ASISA")
        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        
        if st.button("Iniciar Sesión"):
            # Aquí conectarías con Supabase para validar
            if usuario == "director" and password == "demo123":
                st.session_state.logged_in = True
                st.session_state.rol = "director"
                st.session_state.usuario = usuario
                st.rerun()
            else:
                st.error("Credenciales incorrectas")
        return False
    return True

if not check_login():
    st.stop()

# ========================================
# BARRA LATERAL CON FILTROS
# ========================================
st.sidebar.title(f"👤 {st.session_state.usuario}")
st.sidebar.write(f"Rol: {st.session_state.rol}")

st.sidebar.markdown("---")
st.sidebar.info("📄 **Navegación:** Usa el menú lateral para acceder a:\n- 📊 Dashboard KPIs (esta página)\n- 📈 Comparativa Técnica\n- 📖 Documentación")

# Filtros dinámicos según rol
st.sidebar.header("🔍 Filtros")

vertical = st.sidebar.selectbox(
    "Vertical",
    ["Todos", "Venta", "Retención", "Venta (Outbound)", "Venta (Inbound)"]
)

fecha_inicio = st.sidebar.date_input(
    "Fecha inicio",
    datetime.now() - timedelta(days=30)
)

fecha_fin = st.sidebar.date_input(
    "Fecha fin",
    datetime.now()
)

# Mostrar filtro de agente solo si el usuario es director/comercial
if st.session_state.rol in ["director", "comercial"]:
    agente = st.sidebar.selectbox(
        "Agente",
        ["Todos", "Juan Pérez", "María García", "Carlos López"]
    )

granularidad = st.sidebar.radio(
    "Granularidad temporal",
    ["Día", "Semana", "Mes"]
)

# ========================================
# SIMULACIÓN DE DATOS (después conectarás Supabase)
# ========================================
@st.cache_data  # Cachea los datos para mejor performance
def cargar_datos():
    # Simulo datos - después esto será tu query a Supabase
    fechas = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    data = {
        'fecha': fechas,
        'nivel_servicio': np.random.uniform(85, 98, len(fechas)),
        'llamadas_totales': np.random.randint(100, 500, len(fechas)),
        'llamadas_atendidas': np.random.randint(90, 480, len(fechas)),
        'tmo': np.random.uniform(3, 8, len(fechas)),  # minutos
        'tma': np.random.uniform(1, 3, len(fechas)),
        'polizas_vendidas': np.random.randint(5, 50, len(fechas)),
        'presupuestos': np.random.randint(20, 100, len(fechas)),
    }
    
    df = pd.DataFrame(data)
    df['tasa_conversion'] = (df['polizas_vendidas'] / df['presupuestos']) * 100
    return df

df = cargar_datos()

# Filtrar datos según fechas seleccionadas
df_filtrado = df[(df['fecha'] >= pd.Timestamp(fecha_inicio)) & 
                 (df['fecha'] <= pd.Timestamp(fecha_fin))]

# ========================================
# DASHBOARD PRINCIPAL
# ========================================
st.title("📊 Dashboard Call Center ASISA")

# Banner llamativo para documentos ejecutivos
col_banner1, col_banner2, col_banner3 = st.columns([2, 1, 2])
with col_banner2:
    st.markdown("""
        <div style='text-align: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); margin-bottom: 20px;'>
            <a href='?page=documentos_ejecutivos' target='_self' style='text-decoration: none;'>
                <h3 style='color: white; margin: 0; font-size: 18px;'>
                    📑 Documentos para CEO
                </h3>
                <p style='color: #f0f0f0; margin: 5px 0 0 0; font-size: 13px;'>
                    Resumen ejecutivo y presentación técnica completa
                </p>
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown(f"**Período:** {fecha_inicio} - {fecha_fin} | **Vertical:** {vertical}")

# ========================================
# MÉTRICAS PRINCIPALES (KPIs Cards)
# ========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    nivel_servicio = df_filtrado['nivel_servicio'].mean()
    st.metric(
        label="📞 Nivel de Servicio",
        value=f"{nivel_servicio:.1f}%",
        delta=f"{nivel_servicio - 90:.1f}% vs objetivo (90%)"
    )

with col2:
    total_llamadas = df_filtrado['llamadas_totales'].sum()
    st.metric(
        label="📲 Total Llamadas",
        value=f"{total_llamadas:,}",
        delta=f"+{np.random.randint(5, 15)}% vs mes anterior"
    )

with col3:
    tmo_promedio = df_filtrado['tmo'].mean()
    st.metric(
        label="⏱️ TMO Promedio",
        value=f"{tmo_promedio:.1f} min",
        delta=f"-{np.random.uniform(0.1, 0.5):.1f} min"
    )

with col4:
    tasa_conv = df_filtrado['tasa_conversion'].mean()
    st.metric(
        label="💰 Tasa Conversión",
        value=f"{tasa_conv:.1f}%",
        delta=f"+{np.random.uniform(1, 3):.1f}%"
    )

# ========================================
# GRÁFICOS INTERACTIVOS
# ========================================
st.markdown("---")

# Tabs para organizar visualizaciones
tab1, tab2, tab3 = st.tabs(["📈 Tendencias", "📊 Análisis Detallado", "👥 Por Agente"])

with tab1:
    st.subheader("Evolución del Nivel de Servicio")
    
    # Gráfico con Plotly (interactivo)
    fig = px.line(
        df_filtrado, 
        x='fecha', 
        y='nivel_servicio',
        title='Nivel de Servicio a lo largo del tiempo',
        labels={'nivel_servicio': 'Nivel de Servicio (%)', 'fecha': 'Fecha'}
    )
    fig.add_hline(y=90, line_dash="dash", line_color="red", 
                  annotation_text="Objetivo: 90%")
    st.plotly_chart(fig, use_container_width=True)
    
    # Segundo gráfico
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("TMO + TMA")
        df_filtrado['tmo_tma'] = df_filtrado['tmo'] + df_filtrado['tma']
        fig2 = px.area(df_filtrado, x='fecha', y='tmo_tma',
                       title='Tiempo medio total de gestión')
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        st.subheader("Llamadas Diarias")
        fig3 = px.bar(df_filtrado, x='fecha', y='llamadas_totales',
                      title='Volumen de llamadas')
        st.plotly_chart(fig3, use_container_width=True)

with tab2:
    st.subheader("Análisis de Conversión (Venta)")
    
    # Gráfico combinado
    fig4 = px.scatter(
        df_filtrado, 
        x='presupuestos', 
        y='polizas_vendidas',
        size='tasa_conversion',
        color='tasa_conversion',
        title='Relación Presupuestos vs Pólizas Vendidas',
        labels={
            'presupuestos': 'Presupuestos Realizados',
            'polizas_vendidas': 'Pólizas Vendidas'
        }
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    # Usar Seaborn (tu librería favorita)
    st.subheader("Distribución de KPIs")
    fig5, ax = plt.subplots(1, 2, figsize=(12, 4))
    
    sns.histplot(df_filtrado['nivel_servicio'], kde=True, ax=ax[0], color='skyblue')
    ax[0].set_title('Distribución Nivel de Servicio')
    ax[0].axvline(90, color='red', linestyle='--', label='Objetivo')
    ax[0].legend()
    
    sns.boxplot(data=df_filtrado[['tmo', 'tma']], ax=ax[1])
    ax[1].set_title('Comparativa TMO vs TMA')
    
    st.pyplot(fig5)

with tab3:
    st.subheader("Ranking de Agentes")
    
    # Simular datos por agente
    agentes_data = pd.DataFrame({
        'Agente': ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Luis Rodríguez'],
        'Llamadas': [450, 520, 380, 490, 410],
        'Nivel Servicio': [95.2, 92.8, 89.5, 94.1, 91.3],
        'TMO': [4.2, 5.1, 3.8, 4.5, 4.8],
        'Pólizas Vendidas': [28, 35, 22, 31, 26]
    })
    
    # Tabla interactiva
    st.dataframe(
        agentes_data.style.background_gradient(subset=['Nivel Servicio'], cmap='RdYlGn'),
        use_container_width=True
    )
    
    # Gráfico de barras
    fig6 = px.bar(
        agentes_data, 
        x='Agente', 
        y='Pólizas Vendidas',
        color='Nivel Servicio',
        title='Pólizas Vendidas por Agente'
    )
    st.plotly_chart(fig6, use_container_width=True)

# ========================================
# TABLA DE DATOS DETALLADOS
# ========================================
st.markdown("---")
st.subheader("📋 Datos Detallados")

if st.checkbox("Mostrar datos crudos"):
    st.dataframe(
        df_filtrado[['fecha', 'nivel_servicio', 'llamadas_totales', 
                     'tmo', 'tma', 'polizas_vendidas', 'tasa_conversion']],
        use_container_width=True
    )
    
    # Botón de descarga
    csv = df_filtrado.to_csv(index=False)
    st.download_button(
        label="📥 Descargar datos en CSV",
        data=csv,
        file_name=f"datos_asisa_{fecha_inicio}_{fecha_fin}.csv",
        mime="text/csv"
    )

# ========================================
# FOOTER
# ========================================
st.sidebar.markdown("---")
if st.sidebar.button("🚪 Cerrar Sesión"):
    st.session_state.logged_in = False
    st.rerun()