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
# **Puntaje Total:** 6 Puntos
# 
# **Nombre Estudiante(s)**: `Giuseppe Lavarello`

# ### Limpieza de Datos
# ##### Importe de Paquetes

# Para manipulación de data 
import numpy as np
import pandas as pd

# Para visualización de data
from matplotlib import pyplot as plt
import seaborn as sns
import missingno as msno #de NaNs

# Para la normalizacion de la data
from sklearn.preprocessing import MinMaxScaler
  


# ##### Carga de Datos

# Como en el Análisis no cambiamos la data la podemos cargar de la misma manera

df0 = pd.read_csv("..\\data\\raw\\winequality-white.csv", sep=";")


# ##### Manejo de nombres

# Remplazar los espacios en los nombres de las columnas

df0.columns = df0.columns.str.replace(' ', '_')


# 
# ##### Data Faltante (NaNs)

# checkeo de valores nulos
df0.isna().sum()


msno.matrix(df0)


# ##### Data Duplicada

# Checkeo de duplicados
duplicados = df0.duplicated().sum()

# Percentage of duplicated data
porcentaje = duplicados / df0.shape[0] * 100

print(f'{duplicados} filas contienen duplicados, lo que representa el {porcentaje.round(2)}% del total de los datos.')


# Inspeccion de las primeras filas que contienen duplicados

df0[df0.duplicated()].head()


# **Decisión**: Dado que hemos encontrado duplicados, debemos decidir qué hacer con ellos. Esta decisión se toma en base al objetivo final que queremos alcanzar con el conjunto de datos. En este caso, mi plan es intentar realizar algún tipo de regresión para predecir la variable `quality` por lo que simplemente eliminare los duplicados, ya que no agregan nueva información.
# 

# Eliminar duplicados y guardardo del DataFrame en una nueva variable 

df1 = df0.drop_duplicates(keep='first').copy()

# Mostrar las primeras filas del nuevo DataFrame según sea necesario
df1.head()


# Reset del indice

df1.reset_index(drop=True, inplace=True)
df1.head()


# ##### Chequeo de Outliers

# Mostrar estadísticas generales sobre el DataFrame que ayudan a determinar los Outliers

df1.describe()


# Crear un boxplot para visualizar la distribución de todas las variables numéricas y detectar posibles Outliers

# Para crear solo un boxplot para todas las variables, primero debemos normalizar la escala

# Selecciona las columnas numéricas
num_columns = df0.select_dtypes(include=np.number)

# Normalisar valores usando min-max scaling
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(num_columns)

# Creamos un df con la data normalizada
df_normalized = pd.DataFrame(normalized_data, columns=num_columns.columns)

plt.figure(figsize=(10,8))
sns.boxplot(data= df_normalized)
plt.xticks(rotation=45)


plt.show()


# **Decisión**: Al parecer, todas las variables excepto las dos últimas presentan una gran cantidad de Outliers, por lo que tendran que ser estudiadas.
# 

# Determinar el número de filas que contienen valores atípicos para cada variable que necesita ser abordada
X_n = list(num_columns)[:-2]
# Calcular el percentil 25 en `X_n`
percentile25 = df1[X_n].quantile(0.25)

# Calcular el percentil 75 en `X_n`
percentile75 = df1[X_n].quantile(0.75)

# Calcular el rango intercuartil en `X_n`
iqr = percentile75 - percentile25

# Definir el límite superior e inferior para valores no atípicos en `X_n`
upper_limit = percentile75 + 1.5 * iqr
lower_limit = percentile25 - 1.5 * iqr
print("Límite inferior:", lower_limit)
print("Límite superior:", upper_limit)

# Identificar el subconjunto de datos que contiene valores atípicos en `X_n`
outliers = df1[(df1[X_n] > upper_limit) | (df1[X_n] < lower_limit)]

# Contar cuántas filas en los datos contienen valores atípicos en `X_n`
print("Número de filas en los datos que contienen valores atípicos en `X_n`:", len(outliers))


# ##### Resolución de Outliers
# 
# **Decisión**: Dado que casi todas las filas presentan valores atípicos en alguna columna, no podemos simplemente eliminarlos. En su lugar, los valores atípicos serán reemplazados por el valor del percentil 90 o del percentil 10, según corresponda.
# 

# Metodo de sima y cima

# Calcular el percentil 10
percentil_10 = df1[X_n].quantile(0.10)
# Calcular el percentil 90
percentil_90 = df1[X_n].quantile(0.90)
# Aplicar una función lambda para reemplazar los outliers con los umbrales definidos anteriormente
for col in X_n:    
    df1[col] = df1[col].apply(lambda x: (
        percentil_10[col] if x < percentil_10[col]
        else percentil_90[col] if x > percentil_90[col] 
        else x))
df1.describe()


# ##### Exporte de la Data para siguiente notebook

df1.to_csv(r'..\data\interim\wine_inter01.csv', index = False)

