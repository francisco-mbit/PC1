# PC1: Consolidación de conocimientos de Pandas, SQL y NoSQL

## Estructura del Proyecto

Este proyecto está organizado de la siguiente manera:

```
C1_GRUPO1/
│── data/                                           # Contiene los datos utilizados en el análisis
│   │── wine_data.db                                # Base de datos SQLite con los datos limpios
│   │── winequality-red.csv                         # Datos de vinos tintos
│   │── winequality-white.csv                       # Datos de vinos blancos
│   │── winequality.names                           # Descripción de los datos
|   |── consulta_Sql_transformada.json              # Exportación de consulta SQL a dataFrame y después a json
|   |── df_with_nparray.json                        # Exportación de dataFrame con columna de numpy aleatorios a json 
|   |── df_with_nparray_float.json                  # Igual que la anterior pero convertida dicha columna a float
|   |── df_with_nparray_float_timestamp.json        # Exportación de dataFrame con columna de fechas aleatorias a json
|   |── df_with_nparray_float_timestamp_iso.json    # Igual que la anterior pero convertida dicha columna a formato ISO
│
│── img/                        # Contiene las capturas de pantalla utilizadas en el notebook
│   │── df_float.png            # Captura de pantalla de df_with_nparray_float.json
│   │── df_nparray.png          # Captura de pantalla de df_with_nparray.json
│   │── df_timestamp_iso.png    # Captura de pantalla de df_with_nparray_float_timestamp_iso.json 
│   │── df_timestamp.png        # Captura de pantalla de df_with_nparray_float_timestamp.json
│
│── notebooks/                  # Contiene los notebooks de análisis
│   │── main_notebook.ipynb     # Notebook principal con todo el proceso
│
│── src/                        # Código fuente del proyecto
│   │── E01_download_data.py    # Descarga de datos
│   │── E02_combine_data.py     # Combinación de datos
│   │── E03_clean_data.py       # Limpieza de datos
│   │── E04_store_sqlite.py     # Almacenamiento en SQLite
│   │── E05_queries_sqlite.py   # Consultas a la base de datos
│   │── E06_export_json.py      # Exportación de datos a JSON
│   │── E07_eda_wine_quality.py # Análisis exploratorio de calidad del vino
│
│── utils/                      # Funciones auxiliares (vacío)
│   │── utils.py                # Funciones de apoyo
│
│── LICENSE                    # Licencia del proyecto
│── README.md                  # Documentación general del proyecto
│── requirements.txt           # Paquetes necesarios, se ha ejecutado con python Python 3.12.9
```

## Flujo de trabajo

### **Carga de datos**: Descarga y lectura de los datasets.  

EJ 1 - Carga de datos.

EJ 2 - Combinar datasets.

### **Preprocesamiento**: Limpieza y combinación de datos.  

EJ 3 - Filtrar atípicos y manejar datos ausentes.

### **Almacenamiento**: Inserción en SQLite y ejecución de consultas.  

EJ 4 - Almacenar los datos limpios en SQLite.

EJ 5 - Realizar 3 consultas en SQLite.

### **Exportación**: Generación de archivos JSONLines para bases de datos NoSQL. 

EJ 6 - Exportar datos a JSONLines.

### **Análisis Exploratorio**: Identificación de patrones en la calidad del vino.  

EJ 7 - Análisis de calidad de los vinos.


Para ejecutar el flujo de trabajo completo, se recomienda abrir y seguir el notebook `main_notebook.ipynb`.

## Objetivo
Este proyecto tiene como objetivo consolidar conocimientos sobre la manipulación de datos con Pandas, el manejo de bases de datos relacionales (SQLite) y la preparación de los datos para una posible inserción en bases de datos 
no relacionales (MongoDB). El tiempo estimado de trabajo es de 2-3 horas por alumno.

---

## Instrucciones detalladas

### 1. Descarga de datos
- Descarga los datasets para vinos tintos y blancos desde la siguiente URL: [Wine Quality Dataset](http://archive.ics.uci.edu/dataset/186/wine+quality).
- Asegúrate de que ambos datasets se encuentren disponibles en tu entorno de trabajo como archivos CSV.
- Idealmente, intenta llevarlo a cabo de manera programática para no tener que hacer operaciones manualmente.

### 2. Combinar los datos
- Usa Pandas para cargar ambos datasets en dataframes en memoria.
- Combina los datos en un único dataframe añadiendo una columna adicional que indique el tipo de vino (`red` o `white`).
- ¿Cuántos registros tenemos? ¿Cuántas variables y de qué tipo?

### 3. Filtrar atípicos y manejar datos ausentes
- Realiza un análisis estadístico o inspección visual de cada columna numérica para identificar valores atípicos.
- Usa Pandas para filtrar y eliminar los datos atípicos y los valores ausentes. Explica en tu entrega qué criterios utilizaste para identificar los atípicos.

### 4. Almacenar los datos limpios en SQLite
- Usa SQLite para almacenar el dataframe limpio en una base de datos persistente.
- Sigue la documentación oficial de SQLite: [SQLite Python Documentation](https://docs.python.org/3/library/sqlite3.html).

### 5. Realizar 3 consultas en SQLite
Basándote en los datos y las columnas del dataset, realiza las siguientes consultas:
1. **Consulta 1**: ¿Cuál es el promedio de calidad (`quality`) por tipo de vino (`type`)?
2. **Consulta 2**: ¿Cuántos vinos tienen un nivel de alcohol superior a 10.5, agrupados por tipo?
3. **Consulta 3**: Obtén el conteo de vinos por nivel de acidez (`fixed acidity`) agrupados en rangos (por ejemplo, de 0-5, 5-10, 10-15).

### 6. Exportar datos a JSONLines
De cara a una potencial insercion en una base de datos noSQL como `mongoDB`, podemos servirnos de pandas para preparar los datos. 
- ¿Qué estructura de datos de python es la más similar a un documento noSQL? 
- Usa Pandas para transformar los datos de una de las consultas en un archivo JSONLines.
- Usa la librería `jsonlines` para guardar el archivo.
- ¿Qué problemas podrían surgir al transformar un dataframe en jsonlines? 
- Añade una columna que sea originalmente un `np.array`,¿qué sucede al transformarlo en jsonlines? 
- Añade una columna que sea originalmente un `pd.datetime`,¿qué sucede al transformarlo en jsonlines?

### 7. Análisis de calidad de los vinos
- Inspecciona qué caracteriza a los vinos tintos y blancos con mayor calidad (`quality`).
- Usa análisis estadístico, gráficos o cualquier técnica que consideres relevante para identificar patrones.

---

## Notas adicionales para la entrega
- Asegúrate de documentar cada paso en tu entrega y justificar tus decisiones (por ejemplo, cómo identificaste los atípicos).
- El entregable principal será un Jupyter notebook con todos los pasos que habéis seguido y las explicaciones que consideréis pertinentes.
- Incluye en un fichero requirements.txt todas las librerías que estés utilizando.
- La entrega se hará tanto a través de Leemons como en el repositorio de Git asignado para el proyecto.
- Cada grupo debe trabajar en su propia rama del repositorio de [Git](https://github.com/francisco-mbit/PC1).
  - Logead el esfuerzo en diferentes commits, asegurándoos de realizar al menos un commit por persona.
  - Realizad un commit final con el mensaje: **ENTREGA FINAL**.

---


