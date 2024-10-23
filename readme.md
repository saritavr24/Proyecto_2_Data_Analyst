# Homicidios por Siniestros Viales en la Ciudad Autónoma de Buenos Aires: Análisis de Datos para la Reducción de Víctimas Fatales

## Tabla de Contenido
1. [Descripción](#descripción)
2. [Dataset](#dataset)
3. [Estructura del Proyecto](#estructura-del-proyecto)
   - [Limpieza de Datos](#limpieza-de-datos)
   - [Análisis Exploratorio de Datos (EDA)](#análisis-exploratorio-de-datos-eda)
   - [Dashboard en Power BI](#dashboard-en-power-bi)
4. [KPIs](#kpis)

## 1. Descripción
A continuación, se presenta un proyecto de análisis de datos basado en un dataset sobre homicidios en siniestros viales ocurridos en la Ciudad Autónoma de Buenos Aires entre 2016 y 2021. El proyecto incluyó un proceso de limpieza, transformación y normalización de datos, seguido de un análisis exploratorio y un estudio detallado de la problemática. Para concluir, se desarrolló un dashboard en Power BI que muestra las conclusiones y propuestas obtenidas a lo largo del análisis.

## 2. Dataset
Para este proyecto se trabajó con la Base de Víctimas Fatales en Siniestros Viales que se encuentra en formato de Excel y contiene dos pestañas de datos:

- HECHOS: Contiene una fila de hecho con id único y las variables temporales, espaciales y participantes asociadas al mismo.
- VICTIMAS: Contiene una fila por cada víctima de los hechos y las variables edad, sexo y modo de desplazamiento asociadas a cada víctima. Se vincula a los HECHOS mediante el id del hecho.
En este link: https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales se encuentran los datos utilizados en el análisis.

## 3. Estructura del Proyecto
Este proyecto consta de las siguientes etapas principales:

### Limpieza de Datos
Se realiza chequeo de nulos, tratamiento de valores faltantes y duplicados, verificaciópn de tipos de dato y se corrigen inconsistencias en las columnas principales.
Se utiliza un diccionario de datos para entender las variables claves de los siniestros viales.

### Análisis Exploratorio de Datos (EDA)
Se realizaron graficos de las variables más importantes, tales como: accidentes por año, mes, día y hora, género, tipo de calle, rango etario, entre otros.
Se identificaron las principales causas y características de los siniestros viales.

### Dashboard en Power BI
Se creó un dashboard interactivo que permite visualizar los patrones más recurrentes en los siniestros viales, realizando un análisis por víctimas, por tiempo y por ubicación, además presenta las conclusiones de todo el análisis realizado y las propuestas para reducir las víctimas fatales en los accidentes.

## 4. KPIs
Estos indicadores clave de rendimiento planteados nos ayudan a entender si se están alcanzando las metas estratégicas o tácticas, permitiendo tomar decisiones informadas para continuar o mejorar con la reducción de siniestros viales.
- Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior.
- Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior.
- Reducir en un 10% la cantidad de accidentes mortales en intersecciones o cruces en el último semestre, en CABA, respecto al semestre anterior.

## 5. Conclusiones
Cantidad de casos: 696 accidentes viales con un total de 717 víctimas.
DE LAS VÍCTIMAS:
-77% de las víctimas son de género masculino.
-42,12% de las víctimas son motos.
-52,16% se encuentran en edades entre 26 y 50 años.
DEL TIEMPO:
-25,62% de los accidentes ocurren en horario de la Mañana.
-70,43% de los accidentes ocurren en Semana.
-Diciembre es el mes con mayor cantidad de casos.
DE LA UBICACIÓN:
-61,64% de los accidentes suceden en Avenidas.
-75,43% de los accidentes ocurre en Cruces.

## 6. Propuestas:
-Campañas de concientización dirigidas a hombres, motociclistas y personas entre 26 y 50 años, es crucial diseñar campañas de seguridad vial enfocadas en estos grupos, resaltando comportamientos de conducción segura, uso de dispositivos de protección, cumplimiento de las normas de tránsito, maniobras evasivas, manejo en condiciones peligrosas, revisiones sobre los factores de riesgo comunes como el cansancio, la distracción al volante y la velocidad.
-Implementar operativos de control de velocidad y alcoholemia en la mañana puede ayudar a reducir los siniestros en este horario.
-Refuerzos de controles de tránsito en Diciembre, cuando los niveles de movilidad y estrés son mayores debido a festividades, pueden ser efectivos para reducir accidentes.
-Dado que más del 60% de los siniestros ocurren en avenidas, sería beneficioso mejorar la señalización, iluminación, y controles de velocidad en estas zonas.
-Implementar dispositivos de seguridad en cruces (semáforos, señales de advertencia, y pasos de peatones mejor señalizados) puede ser crucial para reducir los siniestros en estos puntos conflictivos.
-Colocar cámaras o radares de control de velocidad en las intersecciones más propensas a accidentes.

## Autor
Sarita Vallejo Ramírez
