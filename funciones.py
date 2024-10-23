## FUNCIONES DE UTILIDAD PARA EL EDA:

# Librerías necesarias
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

def verificar_tipo_dato(df):
    '''
    Esta función toma un DataFrame como entrada y devuelve un resumen que incluye información sobre
    los tipos de datos de cada columna.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        pandas.DataFrame: Un DataFrame que contiene el resumen de cada columna, incluyendo:
        - 'nombre_campo': Nombre de cada columna.
        - 'tipo_datos': Tipos de datos únicos presentes en cada columna.
    '''

    mi_dict = {"nombre_campo": [], "tipo_datos": []}

    for columna in df.columns:
        mi_dict["nombre_campo"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
    df_info = pd.DataFrame(mi_dict)
        
    return df_info

def convertir_a_time(x):
    '''
    Esta función acepta diferentes tipos de entrada y trata de convertirlos en objetos de tiempo (time) de Python.
    Si la conversión no es posible, devuelve None.

    Parameters:
        x (str, datetime, or any): El valor que se desea convertir a un objeto de tiempo (time).

    Returns:
        datetime.time or None: Un objeto de tiempo (time) de Python si la conversión es exitosa,
        o None si no es posible realizar la conversión.
    '''
    if isinstance(x, str):
        try:
            return datetime.strptime(x, "%H:%M:%S").time()
        except ValueError:
            return None
    elif isinstance(x, datetime):
        return x.time()
    return x

def verificar_duplicados(df, columna):
    '''
    Verifica y muestra filas duplicadas en un DataFrame basado en una columna específica.

    Esta función toma como entrada un DataFrame y el nombre de una columna específica.
    Luego, identifica las filas duplicadas basadas en el contenido de la columna especificada,
    las filtra y las ordena para una comparación más sencilla.

    Parameters:
        df (pandas.DataFrame): El DataFrame en el que se buscarán filas duplicadas.
        columna (str): El nombre de la columna basada en la cual se verificarán las duplicaciones.

    Returns:
        pandas.DataFrame or str: Un DataFrame que contiene las filas duplicadas filtradas y ordenadas
        o el mensaje "No hay duplicados" si no se encuentran duplicados.
    '''
    # Se filtran las filas duplicadas
    duplicated_rows = df[df.duplicated(subset=columna, keep=False)]
    if duplicated_rows.empty:
        return "No hay duplicados"
    
    # Se ordenan las filas duplicadas
    duplicated_rows_sorted = duplicated_rows.sort_values(by=columna)
    return duplicated_rows_sorted

def ingresa_valor_moda(df, columna):
    '''
    Ingresa los valores faltantes en una columna de un DataFrame con el valor más frecuente.

    Esta función reemplaza los valores "SD" con NaN en la columna especificada,
    luego calcula el valor más frecuente en esa columna y utiliza ese valor
    para modificar los valores faltantes (NaN).

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene la columna a ser imputada.
        columna (str): El nombre de la columna en la que se realizará la imputación.

    Returns:
        None
    '''
    # Se reemplaza 'SD' con NaN en la columna especificada
    df[columna]=df[columna].replace('SD', pd.NA)
    
    # Verifica el valor más frecuente en la columna
    valor_frecuente= df[columna].mode().iloc[0]
    print('El valor más frecuente de', columna, 'es:', valor_frecuente)

    # Se modifican los valores NaN, con el valor más frecuente
    df[columna].fillna(valor_frecuente, inplace=True)

def ingresa_edad_segun_sexo(df):
    '''
    Imputa valores faltantes en la columna 'Edad' utilizando la edad promedio según el sexo.

    Esta función reemplaza los valores "SD" con NaN en la columna 'Edad', calcula la edad promedio
    para cada grupo de sexo (Femenino y Masculino), imprime los promedios calculados y
    luego llena los valores faltantes en la columna 'Edad' utilizando el promedio correspondiente
    al género al que pertenece cada fila en el DataFrame.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene la columna 'Edad' a ser imputada.

    Returns:
        None
    '''
    # Reemplaza 'SD' con NaN en la columna 'Edad'.
    df['Edad']= df['Edad'].replace('SD', pd.NA)

    # Se calcula el valor promedio de la edad, para cada sexo.
    promedio_por_genero= df.groupby('Sexo')['Edad'].mean()
    print(f'La edad promedio de Femenino es {round(promedio_por_genero["FEMENINO"])} y de Masculino es {round(promedio_por_genero["MASCULINO"])}')

    # Modificamos los valores NaN en 'Edad', con los valores correspondientes en cada género y
    # se verifica fila por fila, si el valor en 'Edad' es NaN, se aplica la función, sino se devuelve el valor original.
    df['Edad']= df.apply(lambda row: promedio_por_genero[row['Sexo']] if pd.isna(row['Edad']) else row['Edad'], axis=1)

    # Convertimos el valor ingresado a tipo int
    df['Edad']= df['Edad'].astype(int)

def accidentes_tipo_de_calle(df):
    '''
    Genera un resumen de los accidentes de tráfico por tipo de calle y cruce.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de accidentes por tipo de calle.
    * Un gráfico de torta que muestra la cantidad de accidentes en cruces.
    
    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se crea el gráfico
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Gráfico 1: Cantidad de accidentes por tipo de calle (barras)
    sns.countplot(data=df, x='Tipo de calle', ax=axes[0])
    axes[0].set_title('Cantidad de accidentes por tipo de calle')
    axes[0].set_ylabel('Cantidad de accidentes')

    # Gráfico 2: Cantidad de accidentes en cruces (torta)
    # Agrupar por la columna 'Cruce' y contar las ocurrencias
    cruce_counts = df['Cruce'].value_counts()

    # Crear gráfico de torta
    axes[1].pie(cruce_counts, labels=cruce_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'))
    axes[1].set_title('Distribución de accidentes en cruces')

    # Asegurarse de que el gráfico de torta esté bien circular
    axes[1].axis('equal')  

    # Mostrar los gráficos
    plt.tight_layout()
    plt.show()

def graficar_histograma_accidentes_hora(df, columna_hora, bins=24):
    '''
    Función para graficar un histograma de la distribución de accidentes por hora del día con más etiquetas en el eje x.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos.
        columna_hora (str): El nombre de la columna que contiene las horas (en formato HH).
        bins (int, opcional): Cantidad de barras en el histograma. Por defecto es 24 para las 24 horas del día.
    
    Returns:
        None
    '''
    plt.figure(figsize=(10,6))  # Tamaño del gráfico

    # Graficar el histograma
    sns.histplot(df[columna_hora], bins=bins, kde=False, color='skyblue')

    # Añadir etiquetas y título
    plt.title('Distribución de Accidentes por Hora del Día', fontsize=16)
    plt.xlabel('Hora del Día', fontsize=12)
    plt.ylabel('Cantidad de Accidentes', fontsize=12)

    # Ajustar los ticks del eje x para mostrar todas las horas del día
    horas = np.arange(0, 24, 1)  # Rango de 0 a 23 con pasos de 1 (cada hora)
    plt.xticks(horas)  # Aplicar las horas como ticks en el eje x

    # Mostrar el gráfico
    plt.show()

def cantidad_de_accidentes_por_mes(df):
    '''
    Crea un gráfico de barras que muestra la cantidad de accidentes por mes.

    Esta función toma un DataFrame que contiene datos de accidentes, agrupa los datos por mes
    y crea un gráfico de barras que muestra la cantidad de accidentes para cada mes.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de accidentes con una columna 'Mes'.

    Returns:
        None
    '''
    data= df.groupby('Mes').agg({'Cantidad víctimas':'sum'}).reset_index()

    # Se realiza el gráfico de barras
    plt.figure(figsize=(6,4))
    ax= sns.barplot(data=data, x='Mes', y='Cantidad víctimas', palette= plt.cm.rainbow(np.linspace(0,1, len(data))) )
    ax.set_title('Cantidad de accidentes por mes')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Cantidad de accidentes')

    # Se imprime el resumen
    print(f'El mes con menor cantidad de accidentes tiene {data.min()[1]} accidentes')
    print(f'El mes con mayor cantidad de accidentes tiene {data.max()[1]} accidentes')

    # Se muestra el gráfico
    plt.show()

def rango_etario(edad):
    '''
    Devuelve el rango etario correspondiente a una edad.

    Parameters:
        Edad: La edad de la víctima.

    Returns:
        El rango etario de la víctima.
    '''

    if edad <= 15:
        return 'INFANTES'
    elif edad >= 16 and edad <= 25:
        return 'JOVENES'
    elif edad >= 26 and edad <= 50:
        return 'ADULTOS'
    elif edad >= 51 and edad <= 70:
        return 'ADULTOS MAYORES'
    else:
        return 'ANCIANOS'
    
def accidentes_por_rango_etario(df):
    '''
    Crea una nueva columna llamada 'Rango etario' en el dataframe recibido, 
    y luego crea un gráfico de barras para mostrar la cantidad de accidentes registradas por rango etario.

    Parameters:
        df: El dataframe a procesar.

    Returns:
        El gráfico de barras creado.
    '''

    # se crea una nueva columna llamada 'Rango etario'
    df['Rango etario'] = df['Edad'].apply(lambda edad: rango_etario(edad))

    # Se agrupan los registros por rango etario
    grupos = df.groupby('Rango etario')
       
    # Se crea un gráfico de barras
    return grupos['Edad'].size().plot.bar(figsize=(10, 6), color=['red', 'green', 'blue', 'orange', 'purple'],
                                           xlabel= 'Rango etario', ylabel='Cantidad de accidentes')

def cantidad_accidentes_sexo_rol_victima(df):
    '''
    Genera un resumen de la cantidad de accidentes por sexo, rol y tipo de vehículo en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Gráficos de barras que muestran la cantidad de accidentes por sexo, rol y tipo de vehículo en orden descendente.
    * DataFrames que muestran la cantidad y el porcentaje de accidentes por sexo, rol y tipo de vehículo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se crea el gráfico
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # Definir paleta de colores (naranja para femenino, azul para masculino)
    colores_por_defecto = sns.color_palette()
    colores_invertidos = [colores_por_defecto[0], colores_por_defecto[1]]  # Naranja, Azul
    
    # Gráfico 1: Sexo (aseguramos que los colores sean consistentes)
    sns.countplot(data=df, x='Sexo', ax=axes[0], palette=colores_invertidos)
    axes[0].set_title('Cantidad de accidentes por sexo')
    axes[0].set_ylabel('Cantidad de accidentes')

    # Gráfico 2: Rol (asegurar que los colores coincidan con la misma asignación)
    df_rol = df.groupby(['Rol', 'Sexo']).size().unstack(fill_value=0)
    df_rol[['FEMENINO', 'MASCULINO']].plot(kind='bar', stacked=True, ax=axes[1], color=[colores_por_defecto[1], colores_por_defecto[0]])
    axes[1].set_title('Cantidad de accidentes por rol')
    axes[1].set_ylabel('Cantidad de accidentes')
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].legend().set_visible(False)

    # Gráfico 3: Tipo de vehículo (asegurar que los colores coincidan con la misma asignación)
    df_victima = df.groupby(['Víctima', 'Sexo']).size().unstack(fill_value=0)
    df_victima[['FEMENINO', 'MASCULINO']].plot(kind='bar', stacked=True, ax=axes[2], color=[colores_por_defecto[1], colores_por_defecto[0]])
    axes[2].set_title('Cantidad de accidentes por tipo de vehículo')
    axes[2].set_ylabel('Cantidad de accidentes')
    axes[2].tick_params(axis='x', rotation=45)
    axes[2].legend().set_visible(False)

    # Se muestran los gráficos
    plt.show()

def cantidad_acusados(df):
    '''
    Genera un grafico de la cantidad de acusados en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un grafico que incluye:

    * Un gráfico de barras que muestra la cantidad de acusados en orden descendente.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se ordenan los datos por 'Acusado' en orden descendente por cantidad
    ordenado = df['Acusado'].value_counts().reset_index()
    ordenado = ordenado.rename(columns={'Cantidad': 'Acusado'})
    ordenado = ordenado.sort_values(by='count', ascending=False)
    
    plt.figure(figsize=(15, 4))
    
    # Crear el gráfico de barras
    ax = sns.barplot(data=ordenado, x='Acusado', y='count', order=ordenado['Acusado'])
    ax.set_title('Cantidad de acusados en los accidentes') ; ax.set_ylabel('Cantidad de acusados') 
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # Se muestra el gráfico
    plt.show()



  
