![Wine Quality Prediction](banner.png)L

# Proyecto PC1: Predicción de calidad del vino

![Python Version](https://img.shields.io/badge/python-3.13-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

Este proyecto tiene como objetivo consolidar conocimientos sobre la manipulación de datos con Pandas, el manejo de bases de datos relacionales (SQLite), la preparación de los datos para una posible inserción en bases de datos no relacionales (MongoDB) y el estudio de patrones del dataset para generar un modelo capaz de predecir la calidad del vino

---

# Tabla de contenidos:
1. [Introducción](#proyecto-pc1-predicción-de-calidad-del-vino)
2. [Estructura del Repositorio](#1-estructura-del-repositorio)
3. [Instalación](#2-instalación-y-creación-del-entorno)
4. [Descripción del Dataset](#4-descripción-del-dataset)
5. [Análisis Realizado](#5-análisis-realizado)
6. [Principales Hallazgos](#6-principales-hallazgos)
7. [Posibles Mejoras y Líneas Futuras](#7-posibles-mejoras-y-líneas-futuras)
8. [Cómo Contribuir](#8-cómo-contribuir)

## 1. Estructura del repositorio
```plaintext
├── data/                   # Datos originales y procesados
├── notebooks/              # Notebooks con el código
├── models/                 # Modelos entrenados guardados
├── requirements.txt        # Librerías necesarias para el entorno
├── README.md               # Documentación del proyecto
└── OCG_PC1_Wine_Quality.ipynb  # Notebook principal


## 2. Instalación y creación del entorno
Para ejecutar este proyecto en tu máquina, sigue estos pasos:

### Clona este repositorio:
```bash
git clone https://github.com/oscarcurtog/PC1_Wine_Quality.git
cd PC1_Wine_Quality
```

### Crea y activa un entorno virtual (opcional pero recomendado):
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate  # Windows
```

### Instala las dependencias:
```bash
pip install -r requirements.txt
```

---

## 3. Gestión de Dependencias y Entorno Virtual
Para garantizar la reproducibilidad del entorno y la consistencia entre equipos, se ha utilizado una estrategia basada en pip-tools y pip-sync para la gestión de dependencias.

### Creación de Archivos de Dependencias
Se han definido dos archivos de entrada para gestionar las dependencias del proyecto de manera organizada:

- requirements.in: Contiene las librerías principales necesarias para ejecutar el proyecto sin especificar versiones. Esto permite obtener siempre la versión más reciente compatible.
- dev-requirements.in: Contiene herramientas adicionales necesarias para el desarrollo, como pruebas unitarias, formateo y validación de código.

---

### Generación de requirements.txt y dev-requirements.txt
Para generar los archivos requirements.txt y dev-requirements.txt, que incluyen las versiones bloqueadas de cada librería (junto con sus dependencias indirectas), se usó el siguiente comando:

```bash
pip-compile requirements.in
pip-compile dev-requirements.in
```
---

### Creación y Configuración del Entorno Virtual
El entorno virtual se creó con Conda siguiendo estos pasos:

```bash
conda create --name PC1 python=3.13.1
conda activate PC1
conda install pip
```

### Instalación de Dependencias con pip-sync
Para instalar todas las dependencias especificadas en los archivos requirements.txt y dev-requirements.txt, se usó:

```bash
pip-sync requirements.txt dev-requirements.txt
```
¿Por qué pip-sync?
Asegura que solo las librerías especificadas en requirements.txt y dev-requirements.txt estén instaladas, evitando conflictos con otras versiones en el entorno.

Para más información sobre la instalación de librerías y configuración del entorno, consulta el documento [aquí](Instalacion_librerias.pdf).

## 4. Descripción del Dataset
El dataset proviene del repositorio de [UCI Machine Learning](http://archive.ics.uci.edu/dataset/186/wine+quality) y contiene características fisicoquímicas de vinos tintos y blancos, junto con una evaluación de calidad numérica .
Cada vino ha sido clasificado en una escala del 0 al 10, donde valores más altos representan mejor calidad.

Variables principales del dataset:

- fixed acidity: Nivel de acidez fija.
- volatile acidity: Nivel de acidez volátil.
- citric acid: Contenido de ácido cítrico.
- residual sugar: Cantidad de azúcar residual.
- chlorides: Nivel de cloruros en el vino.
- free sulfur dioxide: Dióxido de azufre libre.
- total sulfur dioxide: Dióxido de azufre total.
- density: Densidad del vino.
- pH: Nivel de pH del vino.
- sulphates: Nivel de sulfatos.
- alcohol: Porcentaje de alcohol.
- quality: Variable objetivo (target) que mide la calidad del vino.

---

## 5. Análisis Realizado

### Exploración de datos

Análisis descriptivo de las variables.
Identificación de valores atípicos y correlaciones.

### Preprocesamiento

Tratamiento de datos nulos (aunque en este caso no había).
Normalización de variables.
Codificación de la variable categórica type-wine.

### Modelado predictivo

Se probaron varios modelos de machine learning para predecir la calidad del vino:
Árboles de decisión -> Precisión: 58%
Random Forest -> Precisión: 60%
XGBoost -> Precisión: 62%
Se compararon métricas de precisión y error.

### Resultados

El mejor modelo alcanzó un 58% de precisión.
Se observó que las variables con mayor impacto en la calidad son...
La calidad del vino parece estar influenciada por aspectos tanto físicos como químicos, pero también puede ser subjetiva.
Para más detalles sobre el análisis, consulta el [notebook principal](notebooks/OCG_PC1_Wine_Quality.ipynb).

---

## 6. Principales Hallazgos

- El nivel de alcohol y la acidez volátil son factores críticos para determinar la calidad del vino.
- Los vinos blancos tienden a tener mayores niveles de azúcar residual y dióxido de azufre en comparación con los tintos.
- El modelo no logra predecir con 100% de precisión, lo que indica que la evaluación de la calidad tiene cierto grado de subjetividad.
- Se observó una dispersión media de 0,9, lo que significa que aunque el modelo no acierta exactamente, muchas veces se aproxima al valor real.

---

## 7. Posibles Mejoras y Líneas Futuras

- Incorporar técnicas de ajuste de hiperparámetros (GridSearch, RandomSearch) para mejorar la precisión del modelo.
- Utilizar más modelos avanzados como redes neuronales para comparar su desempeño.
- Aplicar técnicas de selección de características (como Recursive Feature Elimination o Permutation Importance) para ver si hay variables irrelevantes.
- Realizar análisis más detallado con SHAP para entender mejor las influencias de cada variable en la predicción.
- Explorar otros datasets similares para validar los resultados.

---

## 8. Cómo Contribuir

Pasos para contribuir:
8.1 Haz un fork del repositorio.
8.2 Crea una nueva rama (git checkout -b feature-nombre).
8.3️ Realiza cambios y confirma los commits (git commit -m "Descripción del cambio").
8.4️ Envía un Pull Request.

## Licencia
Este proyecto está licenciado bajo la licencia MIT.  
Consulta el archivo [LICENSE](LICENSE) para más detalles.
