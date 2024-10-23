# Homicidios por Siniestros Viales en la Ciudad Autónoma de Buenos Aires: Análisis de Datos para la Reducción de Víctimas Fatales

## Tabla de Contenido
1. [Título del Proyecto](#título-del-proyecto)
2. [Descripción](#descripción)
3. [Estructura del Proyecto](#estructura-del-proyecto)
   - [Limpieza de Datos](#limpieza-de-datos)
   - [Análisis Exploratorio de Datos (EDA)](#análisis-exploratorio-de-datos-eda)
   - [ETL](#etl)
   - [Dashboard en Power BI](#dashboard-en-power-bi)
4. [Requerimientos](#requerimientos)
5. [Instrucciones de Instalación](#instrucciones-de-instalación)
6. [Uso](#uso)
7. [Dashboard](#dashboard)
8. [Licencia](#licencia)

## 1. Título del Proyecto
Homicidios por Siniestros Viales en la Ciudad Autónoma de Buenos Aires (CABA)

## 2. Descripción
Este proyecto de Data Science se centra en el análisis de homicidios derivados de siniestros viales en la Ciudad Autónoma de Buenos Aires (CABA). Utilizando una base de datos sobre estos incidentes, el objetivo es explorar patrones y tendencias, así como realizar una limpieza y transformación de los datos para su posterior visualización mediante un dashboard en Power BI.

Objetivos principales:

- Limpieza de datos y preparación para el análisis.
- Análisis exploratorio de datos (EDA) para detectar patrones relevantes.
- Creación de un dashboard interactivo en Power BI para visualizar los resultados.

## 3. Estructura del Proyecto
Este proyecto consta de las siguientes etapas principales:

### Limpieza de Datos
Se eliminan valores faltantes y se corrigen inconsistencias en las columnas principales.
Se utiliza un diccionario de datos para entender las variables claves de los siniestros viales.

### Análisis Exploratorio de Datos (EDA)
Se realizaron visualizaciones de las variables más importantes, tales como: año del homicidio, relación entre acusados y fallecidos, y análisis de la tasa de homicidios por cada 100,000 habitantes.
Se identificaron las principales causas y características de los siniestros viales que resultan en homicidios.

### ETL
Los datos fueron procesados y transformados en un formato limpio, lo que permitió su análisis y preparación para el dashboard en Power BI.

### Dashboard en Power BI
Se creó un dashboard interactivo que permite a los usuarios visualizar los principales hallazgos y métricas relevantes.

## 4. Requerimientos
Las siguientes librerías son necesarias para ejecutar el análisis:

```bash
pip install pandas numpy seaborn matplotlib
```

## 5. Instrucciones de Instalación
Clona este repositorio y accede al proyecto localmente:
```bash
git clone https://github.com/saritavr24/Proyecto_2_Data_Analyst
cd Proyecto_2_Data_Analyst
```

Ejecuta el archivo Jupyter Notebook para reproducir el análisis:

```bash
jupyter notebook EDA.ipynb
```

## 6. Uso
Una vez que hayas ejecutado el notebook, el DataFrame final datos_homicidios_final.csv se generará y estará listo para ser utilizado en el dashboard de Power BI. A continuación, se puede cargar este archivo en Power BI para visualizar los datos de forma interactiva.

7. Dashboard
El dashboard se encuentra en el archivo Dashboard.pbix (disponible en este repositorio) y puede ser visualizado utilizando Power BI Desktop. Si el dashboard está publicado, también puedes acceder mediante el siguiente enlace: Dashboard en Power BI.

8. Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
