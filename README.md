# Dashboard Call Center ASISA

Dashboard interactivo para visualización de KPIs del Call Center de ASISA, desarrollado con Streamlit.

## Características

- Visualización de métricas clave (KPIs):
  - Nivel de Servicio
  - Total de Llamadas
  - TMO (Tiempo Medio Operativo)
  - Tasa de Conversión
- Gráficos interactivos con Plotly y Seaborn
- Filtros dinámicos por vertical, fecha y agente
- Sistema de autenticación básico
- Análisis detallado por agente
- Exportación de datos a CSV

## Instalación Local

1. Clonar el repositorio:
```bash
git clone https://github.com/mariavictoriacairos/asisa-dashboard.git
cd asisa-dashboard
```

2. Crear entorno virtual e instalar dependencias:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```bash
streamlit run dashboard.py
```

## Credenciales de Prueba

- Usuario: `director`
- Contraseña: `demo123`

## Tecnologías

- Streamlit
- Pandas
- Plotly
- Seaborn
- Matplotlib
- NumPy

## Demo

Próximamente disponible en Streamlit Cloud
