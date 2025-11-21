"""
Script para generar gráficos comparativos PowerBI vs Streamlit+Supabase
Para la presentación técnica ASISA
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots

# Configuración estética
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

# Colores corporativos
COLOR_POWERBI = '#F2C811'
COLOR_PROPUESTA = '#3ECF8E'
COLOR_NEGATIVO = '#E74C3C'
COLOR_POSITIVO = '#2ECC71'

def grafico_1_comparativa_costes():
    """Comparativa de costes anuales"""
    
    categorias = ['PowerBI Pro\n+ Azure SQL', 'PowerBI Premium\n+ Azure SQL', 
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
        title={
            'text': '💰 Comparativa de Costes Anuales',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2C3E50'}
        },
        yaxis_title='Coste Anual (€)',
        xaxis_title='Solución',
        showlegend=False,
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='lightgray')
    )
    
    # Agregar anotación de ahorro
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
    
    fig.write_html('./grafico_1_costes.html')
    print("✅ Gráfico 1 creado: grafico_1_costes.html")

def grafico_2_rendimiento():
    """Comparativa de tiempo de carga del dashboard"""
    
    soluciones = ['Acceso\nDirecto', 'PowerBI\nDirectQuery', 'PowerBI\nImport Mode', 
                  'Streamlit +\nSupabase ETL']
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
        title={
            'text': '⚡ Comparativa de Rendimiento - Tiempo de Carga Dashboard',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2C3E50'}
        },
        yaxis_title='Tiempo de Carga (segundos)',
        xaxis_title='Solución',
        showlegend=False,
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='lightgray')
    )
    
    # Línea de objetivo (1 segundo)
    fig.add_hline(
        y=1.0, 
        line_dash="dash", 
        line_color="red",
        annotation_text="Objetivo: <1s",
        annotation_position="right"
    )
    
    # Anotación de mejora
    fig.add_annotation(
        x=3, y=0.2,
        text="47x más rápido<br>vs acceso directo",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor=COLOR_POSITIVO,
        ax=0,
        ay=-60,
        bgcolor=COLOR_POSITIVO,
        font=dict(color='white', size=12),
        bordercolor=COLOR_POSITIVO,
        borderwidth=2
    )
    
    fig.write_html('./grafico_2_rendimiento.html')
    print("✅ Gráfico 2 creado: grafico_2_rendimiento.html")

def grafico_3_disponibilidad():
    """Comparativa de disponibilidad del sistema"""
    
    soluciones = ['Acceso Directo\n(sin consolidación)', 
                  'Streamlit + Supabase\n(con ETL)']
    disponibilidad = [70, 99.9]
    colores = [COLOR_NEGATIVO, COLOR_PROPUESTA]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=soluciones,
        y=disponibilidad,
        text=[f'{d}%' for d in disponibilidad],
        textposition='auto',
        marker_color=colores,
        hovertemplate='<b>%{x}</b><br>Disponibilidad: %{y}%<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': '📊 Disponibilidad Estimada del Sistema',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2C3E50'}
        },
        yaxis_title='Disponibilidad (%)',
        xaxis_title='Arquitectura',
        showlegend=False,
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='lightgray', range=[0, 105])
    )
    
    # Línea SLA típico
    fig.add_hline(
        y=99.5, 
        line_dash="dash", 
        line_color="green",
        annotation_text="SLA objetivo: 99.5%",
        annotation_position="right"
    )
    
    fig.write_html('./grafico_3_disponibilidad.html')
    print("✅ Gráfico 3 creado: grafico_3_disponibilidad.html")

def grafico_4_impacto_sistemas():
    """Impacto en sistemas origen - Queries por hora"""
    
    sistemas = ['TUIO', 'ARTEMISA', 'CORE SENDA']
    acceso_directo = [4800, 4800, 4800]
    con_etl = [2, 2, 2]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Acceso Directo',
        x=sistemas,
        y=acceso_directo,
        text=[f'{q:,}' for q in acceso_directo],
        textposition='auto',
        marker_color=COLOR_NEGATIVO,
        hovertemplate='<b>%{x}</b><br>Queries/hora: %{y:,}<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Con ETL Incremental',
        x=sistemas,
        y=con_etl,
        text=[f'{q}' for q in con_etl],
        textposition='auto',
        marker_color=COLOR_PROPUESTA,
        hovertemplate='<b>%{x}</b><br>Queries/hora: %{y}<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': '🔥 Impacto en Sistemas Productivos (Horario Pico 9-11 AM)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2C3E50'}
        },
        yaxis_title='Queries por Hora',
        xaxis_title='Sistema Origen',
        barmode='group',
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='lightgray', type='log'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    # Anotación de reducción
    fig.add_annotation(
        x=2, y=2,
        text="Reducción: 99.96%",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor=COLOR_POSITIVO,
        ax=0,
        ay=-80,
        bgcolor=COLOR_POSITIVO,
        font=dict(color='white', size=14, family='Arial Black'),
        bordercolor=COLOR_POSITIVO,
        borderwidth=2
    )
    
    fig.write_html('./grafico_4_impacto_sistemas.html')
    print("✅ Gráfico 4 creado: grafico_4_impacto_sistemas.html")

def grafico_5_seguridad_comparativa():
    """Matriz de comparación de seguridad"""
    
    caracteristicas = [
        'Certificaciones<br>ISO/SOC',
        'Encriptación<br>en tránsito',
        'Encriptación<br>en reposo',
        'Row Level<br>Security',
        'Backups<br>automáticos',
        'Auditoría<br>completa',
        'GDPR<br>Compliance'
    ]
    
    # Puntuaciones (0-10)
    powerbi = [10, 10, 8, 6, 7, 8, 10]
    supabase = [10, 10, 10, 10, 10, 10, 10]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=powerbi,
        theta=caracteristicas,
        fill='toself',
        name='PowerBI + SQL Server',
        line_color=COLOR_POWERBI,
        fillcolor=f'rgba(242, 200, 17, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=supabase,
        theta=caracteristicas,
        fill='toself',
        name='Streamlit + Supabase',
        line_color=COLOR_PROPUESTA,
        fillcolor=f'rgba(62, 207, 142, 0.3)'
    ))
    
    fig.update_layout(
        title={
            'text': '🔒 Comparativa de Características de Seguridad',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2C3E50'}
        },
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickvals=[0, 2, 4, 6, 8, 10],
                ticktext=['0', '2', '4', '6', '8', '10']
            )
        ),
        showlegend=True,
        height=600,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5
        )
    )
    
    fig.write_html('./grafico_5_seguridad.html')
    print("✅ Gráfico 5 creado: grafico_5_seguridad.html")

def grafico_6_timeline():
    """Timeline de implementación"""
    
    df = pd.DataFrame([
        dict(Task="Setup Infraestructura", Start='2024-11-25', Finish='2024-12-08', Resource='Fase 1'),
        dict(Task="Desarrollo ETL", Start='2024-12-09', Finish='2024-12-22', Resource='Fase 2'),
        dict(Task="Dashboard Core", Start='2024-12-23', Finish='2025-01-12', Resource='Fase 3'),
        dict(Task="Testing y Ajustes", Start='2025-01-13', Finish='2025-01-26', Resource='Fase 4'),
        dict(Task="Despliegue Producción", Start='2025-01-27', Finish='2025-02-02', Resource='Fase 5'),
    ])
    
    fig = px.timeline(
        df, 
        x_start="Start", 
        x_end="Finish", 
        y="Task",
        color="Resource",
        title="📅 Timeline de Implementación - 10 Semanas",
        color_discrete_sequence=[COLOR_PROPUESTA, '#3498DB', '#9B59B6', '#E67E22', '#E74C3C']
    )
    
    fig.update_yaxes(categoryorder="total ascending")
    fig.update_layout(
        height=400,
        showlegend=True,
        title_x=0.5,
        title_font_size=20,
        title_font_color='#2C3E50',
        xaxis_title='Fecha',
        yaxis_title='Tarea'
    )
    
    fig.write_html('./grafico_6_timeline.html')
    print("✅ Gráfico 6 creado: grafico_6_timeline.html")

def grafico_7_roi():
    """ROI acumulado a lo largo del tiempo"""
    
    meses = list(range(0, 37))
    
    # Costes PowerBI Pro (acumulado)
    coste_powerbi = [1855 * m for m in meses]
    
    # Costes Solución Propuesta (inversión inicial + mensual)
    inversion_inicial = 18000
    coste_propuesta = [inversion_inicial + (80 * m) for m in meses]
    
    # Calcular ahorro
    ahorro = [coste_powerbi[i] - coste_propuesta[i] for i in range(len(meses))]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=meses,
        y=coste_powerbi,
        name='PowerBI (acumulado)',
        line=dict(color=COLOR_POWERBI, width=3),
        mode='lines'
    ))
    
    fig.add_trace(go.Scatter(
        x=meses,
        y=coste_propuesta,
        name='Streamlit + Supabase (acumulado)',
        line=dict(color=COLOR_PROPUESTA, width=3),
        mode='lines'
    ))
    
    fig.add_trace(go.Scatter(
        x=meses,
        y=ahorro,
        name='Ahorro neto',
        line=dict(color=COLOR_POSITIVO, width=3, dash='dash'),
        mode='lines',
        fill='tozeroy',
        fillcolor='rgba(46, 204, 113, 0.1)'
    ))
    
    fig.update_layout(
        title={
            'text': '💰 Análisis de ROI - Coste Acumulado en 3 Años',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2C3E50'}
        },
        xaxis_title='Meses desde implementación',
        yaxis_title='Coste Acumulado (€)',
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='lightgray'),
        xaxis=dict(gridcolor='lightgray'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode='x unified'
    )
    
    # Punto de break-even
    breakeven_mes = next((i for i, v in enumerate(ahorro) if v > 0), None)
    if breakeven_mes:
        fig.add_vline(
            x=breakeven_mes,
            line_dash="dash",
            line_color="green",
            annotation_text=f"Break-even: Mes {breakeven_mes}",
            annotation_position="top"
        )
    
    # Ahorro a 3 años
    ahorro_3_años = ahorro[-1]
    fig.add_annotation(
        x=36, y=ahorro_3_años,
        text=f"Ahorro 3 años: €{ahorro_3_años:,.0f}",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor=COLOR_POSITIVO,
        ax=-100,
        ay=-50,
        bgcolor=COLOR_POSITIVO,
        font=dict(color='white', size=12),
        bordercolor=COLOR_POSITIVO,
        borderwidth=2
    )
    
    fig.write_html('./grafico_7_roi.html')
    print("✅ Gráfico 7 creado: grafico_7_roi.html")

def grafico_8_matriz_decision():
    """Matriz de decisión: Rendimiento vs Coste"""
    
    soluciones = [
        'Acceso Directo',
        'PowerBI DirectQuery',
        'PowerBI Import Mode',
        'PowerBI Premium',
        'Streamlit + Supabase'
    ]
    
    # Eje X: Rendimiento (tiempo carga invertido, más a la derecha = mejor)
    rendimiento_score = [1, 1, 10, 10, 12]  # Basado en velocidad
    
    # Eje Y: Coste (invertido, más arriba = más económico)
    coste_anual = [1000, 22260, 22260, 52644, 960]
    coste_score = [100000/c for c in coste_anual]  # Invertir para que menor coste = más arriba
    
    tamaños = [50, 80, 80, 80, 100]  # Tamaño de los círculos
    
    colores_custom = [COLOR_NEGATIVO, COLOR_POWERBI, COLOR_POWERBI, COLOR_POWERBI, COLOR_PROPUESTA]
    
    fig = go.Figure()
    
    for i, sol in enumerate(soluciones):
        fig.add_trace(go.Scatter(
            x=[rendimiento_score[i]],
            y=[coste_score[i]],
            mode='markers+text',
            name=sol,
            text=[sol],
            textposition='top center',
            marker=dict(
                size=tamaños[i],
                color=colores_custom[i],
                line=dict(width=2, color='white')
            ),
            hovertemplate=f'<b>{sol}</b><br>Coste: €{coste_anual[i]:,}/año<extra></extra>'
        ))
    
    fig.update_layout(
        title={
            'text': '🎯 Matriz de Decisión: Rendimiento vs Coste',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2C3E50'}
        },
        xaxis_title='Rendimiento (velocidad carga) →',
        yaxis_title='Ahorro (menor coste) →',
        height=600,
        plot_bgcolor='white',
        showlegend=False,
        xaxis=dict(
            gridcolor='lightgray',
            showticklabels=False,
            zeroline=False
        ),
        yaxis=dict(
            gridcolor='lightgray',
            showticklabels=False,
            zeroline=False
        )
    )
    
    # Cuadrantes
    fig.add_hline(y=coste_score[2], line_dash="dash", line_color="gray", opacity=0.3)
    fig.add_vline(x=rendimiento_score[2], line_dash="dash", line_color="gray", opacity=0.3)
    
    # Anotaciones de cuadrantes
    fig.add_annotation(x=11, y=max(coste_score)*0.95, text="⭐ ÓPTIMO", showarrow=False, 
                      font=dict(size=16, color=COLOR_POSITIVO), bgcolor='rgba(46, 204, 113, 0.1)')
    
    fig.write_html('./grafico_8_matriz_decision.html')
    print("✅ Gráfico 8 creado: grafico_8_matriz_decision.html")

def crear_infografia_resumen():
    """Crear infografía resumen con métricas clave"""
    
    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=(
            '💰 Ahorro Anual', 
            '⚡ Mejora Rendimiento',
            '📊 Disponibilidad',
            '🔥 Reducción Carga',
            '🔒 Nivel Seguridad',
            '⏱️ Tiempo Implementación'
        ),
        specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}],
               [{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]]
    )
    
    # Métrica 1: Ahorro
    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=21300,
        number={'prefix': "€", 'suffix': '/año', 'font': {'size': 40}},
        delta={'reference': 0, 'relative': False, 'increasing': {'color': COLOR_POSITIVO}},
        domain={'x': [0, 1], 'y': [0, 1]}
    ), row=1, col=1)
    
    # Métrica 2: Rendimiento
    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=47,
        number={'suffix': 'x', 'font': {'size': 40}},
        delta={'reference': 1, 'increasing': {'color': COLOR_POSITIVO}},
        domain={'x': [0, 1], 'y': [0, 1]}
    ), row=1, col=2)
    
    # Métrica 3: Disponibilidad
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=99.9,
        number={'suffix': '%', 'font': {'size': 40}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': COLOR_PROPUESTA},
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 99.5
            }
        },
        domain={'x': [0, 1], 'y': [0, 1]}
    ), row=1, col=3)
    
    # Métrica 4: Reducción carga
    fig.add_trace(go.Indicator(
        mode="number",
        value=99.96,
        number={'suffix': '%', 'font': {'size': 40, 'color': COLOR_POSITIVO}},
        domain={'x': [0, 1], 'y': [0, 1]}
    ), row=2, col=1)
    
    # Métrica 5: Seguridad
    fig.add_trace(go.Indicator(
        mode="number",
        value=10,
        number={'suffix': '/10', 'font': {'size': 40, 'color': COLOR_PROPUESTA}},
        domain={'x': [0, 1], 'y': [0, 1]}
    ), row=2, col=2)
    
    # Métrica 6: Tiempo
    fig.add_trace(go.Indicator(
        mode="number",
        value=10,
        number={'suffix': ' semanas', 'font': {'size': 40}},
        domain={'x': [0, 1], 'y': [0, 1]}
    ), row=2, col=3)
    
    fig.update_layout(
        height=600,
        title={
            'text': '📊 RESUMEN EJECUTIVO - Métricas Clave',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'color': '#2C3E50'}
        },
        showlegend=False
    )
    
    fig.write_html('./grafico_9_infografia_resumen.html')
    print("✅ Gráfico 9 creado: grafico_9_infografia_resumen.html")

if __name__ == "__main__":
    print("🎨 Generando gráficos para presentación técnica ASISA...\n")
    
    grafico_1_comparativa_costes()
    grafico_2_rendimiento()
    grafico_3_disponibilidad()
    grafico_4_impacto_sistemas()
    grafico_5_seguridad_comparativa()
    grafico_6_timeline()
    grafico_7_roi()
    grafico_8_matriz_decision()
    crear_infografia_resumen()
    
    print("\n✅ ¡Todos los gráficos generados exitosamente!")
    print("\n📁 Archivos creados:")
    print("   - grafico_1_costes.html")
    print("   - grafico_2_rendimiento.html")
    print("   - grafico_3_disponibilidad.html")
    print("   - grafico_4_impacto_sistemas.html")
    print("   - grafico_5_seguridad.html")
    print("   - grafico_6_timeline.html")
    print("   - grafico_7_roi.html")
    print("   - grafico_8_matriz_decision.html")
    print("   - grafico_9_infografia_resumen.html")
    print("\n💡 Abre los archivos HTML en cualquier navegador para ver los gráficos interactivos")
