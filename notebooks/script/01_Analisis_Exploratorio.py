#!/usr/bin/env python
# coding: utf-8

# 
# <div>
# <img src="https://i.ibb.co/v3CvVz9/udd-short.png" width="150"/>
#     <br>
#     <strong>Universidad del Desarrollo</strong><br>
#     <em>Magíster en Data Science</em><br>
#     <em>Profesor: Víctor Navarro Aránguiz</em><br>
# 
# </div>
# 
# # Python para Data Science: Proyecto final
# *15 de Julio de 2024*
# 
# **Fecha de Entrega**: 04 de Agosto de 2024
# 
# **Objetivos:**
#   - Aplicar los conceptos aprendidos en clases.
#   - Realizar el análisis de un dataset de su preferencia.
#   - Familiarizarse con el manejo de versiones a través de Git.
# 
# **Puntaje Total:** 5 Puntos
# 
# **Nombre Estudiante(s)**: `Giuseppe Lavarello`

# ### Análisis Exploratorio
# ##### Importe de Paquetes
# 

# Para manipulación de data 
import numpy as np
import pandas as pd

# Para visualización de data
from matplotlib import pyplot as plt
import seaborn as sns
import missingno as msno #de NaNs



# ##### Carga de Datos

df0 = pd.read_csv("..\\data\\raw\\winequality-white.csv", sep=";")


# ##### Recopilación de información básica sobre los datos

# Mostrar las primeras 10 filas de los datos

df0.head(10)


# Mostrar 10 filas aleatorias de los datos

df0.sample(10)


# # Informacion de las columnas
# 
# | Columna                 | Cuenta de No Nulos | Dtype   |
# |-------------------------|----------------|---------|
# | fixed acidity           | 4898   | float64 |
# | volatile acidity        | 4898   | float64 |
# | citric acid             | 4898   | float64 |
# | residual sugar          | 4898   | float64 |
# | chlorides               | 4898   | float64 |
# | free sulfur dioxide     | 4898   | float64 |
# | total sulfur dioxide    | 4898   | float64 |
# | density                 | 4898   | float64 |
# | pH                      | 4898   | float64 |
# | sulphates               | 4898   | float64 |
# | alcohol                 | 4898   | float64 |
# | quality                 | 4898   | int64   |
# 
# [Click aqui para informacion detallada de cada caracteristica](https://www.oiv.int/standards/compendium-of-international-methods-of-wine-and-must-analysis)

# - **fixed acidity**: La acidez fija, medida en **meq/L**, se calcula a partir de la diferencia entre la acidez total y la acidez volátil.
# - **volatile acidity**: La acidez volátil, expresada en **meq/L**, se deriva de los ácidos de la serie acética presentes en el vino en estado libre y combinados como sales.
# - **citric acid**:  La cantidad de acido citrico precente en el vino, medido en **mg/L**.
# - **residual sugar**: El azúcar residual, medido en **gr/L**, que proviene de los azúcares naturales de la uva que quedan en el vino después de que finaliza la fermentación alcohólica.
# - **chlorides**: Numero de **mL** de compuestos conteniendo iones negativos de Cloro o que tiene un enlase unico con un atomo de CL.
# - **free sulfur dioxide**: El dióxido de azufre libre, medido en **mg/L**, se define como el dióxido de azufre presente en el mosto o vino en las siguientes formas: H₂SO₃ y HSO₃⁻.
# - **total sulfur dioxide**: El dióxido de azufre total, medido en **mg/L**, se define como la suma de todas las formas diferentes de dióxido de azufre presentes en el vino.
# - **density**: La densidad del vino, medida en **g/mL**
# - **pH**: El pH del vino, medido en unidades de **pH**
# - **sulphates**: Los sulfatos son sales derivadas del ácido sulfúrico (H₂SO₄), medido en **mg/L**
# - **alcohol**: La graduación alcohólica por volumen (ABV). Se expresa como **% vol.**.
# - **quality**: La medición subjetiva de la calidad del vino.
# 

# ##### Recopilación de información básica sobre el conjunto de datos

df0.info()


# ##### Recopilación de estadísticas descriptivas sobre los datos

df0.describe()


# ##### Mostrar el tamaño del DataFrame

df0.shape


# ##### Visualizar NaNs

msno.matrix(df0)


# ##### Buscamos duplicados

df0[df0.duplicated(keep="first")].copy()

