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
# **Puntaje Total:** 4 Puntos
# 
# **Nombre Estudiante(s)**: `Giuseppe Lavarello`

# ### Creación de Variables
# ##### Importe de Paquetes

# Para manipulación de data 
import numpy as np
import pandas as pd

# Para visualización de data
from matplotlib import pyplot as plt
import seaborn as sns

  


# ##### Carga de Datos

# Cargar la versión intermedia del dataset

df0 = pd.read_csv("..\\data\\interim\\wine_inter01.csv")


# Crear una muestra de los valores
df0.sample(5)


# ##### Creacion de variables
# - Total acidity

# Se crea la feature `total_acidity` en base a la suma de las características de acidez
df0['total_acidity'] = df0["fixed_acidity"] + df0["volatile_acidity"]


df0.head()


df0[["fixed_acidity","volatile_acidity","total_acidity","quality"]].corr()


# **Desición** Se puede ver que la variable `total_acidity` no precenta una "mayor" (como en mas lejos de 0) correlacion con la variable `quality` por lo que sera descartada pues no impulza el objetivo de crear una regresión
# 
# 

df0.drop(columns="total_acidity",inplace=True)


# 
# 
# - Fixed sulfur dioxide

df0['fixed_sulfur_dioxide'] = df0['total_sulfur_dioxide'] - df0['free_sulfur_dioxide']


df0.head()


df0[["free_sulfur_dioxide","total_sulfur_dioxide","fixed_sulfur_dioxide","quality"]].corr()


# **Decisión**: Aquí se ve que la nueva variable `fixed_sulfur_dioxide` presenta una mayor correlación con la variable `quality` que las dos variables que la forman, por lo que la mantendremos. Esto nos permitira utilizarla en vez de las 2 anteriores a la hora de crear la regresión disminuyendo la dimensionalidad total del problema.
# 
