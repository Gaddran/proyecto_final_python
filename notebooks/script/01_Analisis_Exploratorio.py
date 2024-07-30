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


# Recopilación de información básica sobre el conjunto de datos
df0.info()


# Recopilación de estadísticas descriptivas sobre los datos
df0.describe()


# Mostrar el tamaño del DataFrame
df0.shape


# Visualizar NaNs
msno.matrix(df0)




