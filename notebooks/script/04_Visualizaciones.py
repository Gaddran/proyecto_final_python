#!/usr/bin/env python
# coding: utf-8

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

# ### Visualización
# ##### Importe de Paquetes

# Para manipulación de data 
from re import S
import numpy as np
import pandas as pd
import scipy

# Para visualización de data
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_theme()


df0 = pd.read_csv(r'..\data\interim\wine_inter02.csv',index_col=0)


df0.head()


# En el siguiente grafico podemos ver las features con minimo efecto en la variable `quality`

# Se grafican el efecto de las siguientes columnas ["volatile_acidity","citric_acid","chlorides","pH","density","sulphates"]
plt.figure(figsize=(15,7))

sns.lineplot(data=df0, x="quality",y="volatile_acidity",label="Volatile Acidity")
sns.lineplot(data=df0, x="quality",y="citric_acid",label="Citric Acid")
sns.lineplot(data=df0, x="quality",y="chlorides",label="Chlorides")
sns.lineplot(data=df0, x="quality",y="pH",label="pH")
sns.lineplot(data=df0, x="quality",y="density",label="density")
sns.lineplot(data=df0, x="quality",y="sulphates",label="Sulphates")

plt.ylabel("Cantidad")
plt.title("Impacto en quality")
plt.legend()
plt.show()


plt.figure(figsize=(15,7))
sns.lineplot(data=df0, x="quality",y="alcohol",label="Alcohol")
plt.ylabel("Cantidad")
plt.title("Impacto del contenido de Alcohol en quality")
plt.legend()
plt.show()


def feat_plot(feature):
    fig, ax= plt.subplots(1, 2, figsize=(16, 6))
    sns.histplot(feature,ax=ax[0])
    sns.boxplot(feature,ax=ax[1], orient="h")


num_feat = df0.select_dtypes(exclude = 'object').drop(columns="quality")


for i in num_feat.columns:
    feat_plot(num_feat[i])

