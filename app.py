import pandas as pd
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Dashboard interactivo de notas", layout="wide"
)

# Título principal
st.title("Dashboard interactivo de notas")
st.markdown(
    "Explora los resultados de un curso combinando filtros. **Promedio:** 50% de cada evaluación. **Aprobación del ejercicio:** promedio mayor o igual a 4,0. Datos ficticios."
)
st.markdown("---")

# Datos ficticios basados en la imagen
data = {
    "ID": [f"E0{i}" if i < 10 else f"E{i}" for i in range(1, 13)],
    "Estudiante": [
        "Ana",
        "Andrés",
        "Camila",
        "Carla",
        "Diego",
        "Juan",
        "Lucía",
        "Luis",
        "Marta",
        "Pedro",
        "Sofía",
        "Tomás",
    ],
    "Sexo": [
        "Mujer",
        "Hombre",
        "Mujer",
        "Mujer",
        "Hombre",
        "Hombre",
        "Mujer",
        "Hombre",
        "Mujer",
        "Hombre",
        "Mujer",
        "Hombre",
    ],
    "Section": ["A", "A", "A", "A", "B", "C", "A", "B", "B", "A", "A", "D"],
    # Ajustamos la letra de la sección para que coincida visualmente o de forma estándar
    "Sección": [
        "A",
        "A",
        "A",
        "A",
        "B",
        "C",
        "C",
        "A",
        "B",
        "D",
        "A",
        "D",
    ],  # Simplificado para el ejemplo
    "Promedio": [
        6.30,
        4.10,
        4.90,
        5.30,
        3.10,
        3.50,
        6.60,
        5.20,
        4.90,
        6.10,
        4.10,
        6.30,
    ],
    "Asistencia (%)": [95, 88, 72, 60, 90, 68, 96, 78, 85, 96, 82, 92],
}

# Normalizamos claves para que coincidan con la tabla visual
df = pd.DataFrame(
    {
        "ID": [
            "E01",
            "E02",
            "E03",
            "E04",
            "E05",
            "E06",
            "E07",
            "E08",
            "E09",
            "E10",
            "E11",
            "E12",
        ],
        "Estudiante": [
            "Ana",
            "Andrés",
            "Camila",
            "Carla",
            "Diego",
            "Juan",
            "Lucía",
            "Luis",
            "Marta",
            "Pedro",
            "Sofía",
            "Tomás",
        ],
        "Sexo": [
            "Mujer",
            "Hombre",
            "Mujer",
            "Mujer",
            "Hombre",
            "Hombre",
            "Mujer",
            "Hombre",
            "Mujer",
            "Hombre",
            "Mujer",
            "Hombre",
        ],
        "Sección": [
            "A",
            "A",
            "A",
            "B",
            "B",
            "B",
            "C",
            "C",
            "C",
            "D",
            "D",
            "D",
        ],
        "Promedio": [
            6.30,
            4.10,
            4.90,
            5.30,
            3.10,
            3.50,
            6.60,
            5.20,
            4.90,
            6.10,
            4.10,
            6.30,
        ],
        "Asistencia (%)": [95, 88, 72, 60, 90, 68, 96, 78, 85, 96, 82, 92],
    }
)

# --- BARRA LATERAL (FILTROS) ---
st.sidebar.header("Datos y filtros")
st.sidebar.text("Carga el archivo de estudiantes")
uploaded_file = st.sidebar.file_uploader(
    "estudia_notas.csv", type=["csv"], label_visibility="collapsed"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

st.sidebar.markdown("---")

# Filtro Sexo
sexos_disponibles = df["Sexo"].unique().tolist()
sexo_seleccionado = st.sidebar.multiselect(
    "Sexo", options=sexos_disponibles, default=sexos_disponibles
)

# Filtro Sección
secciones_disponibles = ["Todas"] + sorted(df["Sección"].unique().tolist())
seccion_seleccionada = st.sidebar.selectbox("Sección", options=secciones_disponibles)

# Filtro Rango de promedio
rango_promedio = st.sidebar.slider(
    "Rango del promedio", min_value=1.0, max_value=7.0, value=(1.0, 7.0)
)

# Filtro Asistencia mínima
asistencia_minima = st.sidebar.number_input(
    "Asistencia mínima (%)", min_value=0, max_value=100, value=0
)

# Aplicar filtros
df_filtrado = df[
    (df["Sexo"].isin(sexo_seleccionado))
    & (df["Promedio"] >= rango_promedio[0])
    & (df["Promedio"] <= rango_promedio[1])
    & (df["Asistencia (%)"] >= asistencia_minima)
]

if seccion_seleccionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Sección"] == seccion_seleccionada]

# Texto de filtros activos
st.markdown(
    f"<small>Filtros activos: Sexo: {', '.join(sexo_seleccionado) if sexo_seleccionado else 'Ninguno'} - Sección: {seccion_seleccionada} - Promedio: {rango_promedio[0]} a {rango_promedio[1]} - Asistencia mínima: {asistencia_minima}%</small
