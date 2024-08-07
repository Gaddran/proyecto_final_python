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

# ### Aplicaciones prácticas
# 
# #### Modelo de Predicción de Calidad
# 
# Desarrollar un modelo de aprendizaje automático para predecir la calidad del vino basado en sus propiedades fisicoquímicas.   
# Esto podría ser utilizado para evaluar la calidad antes de la cata humana, lo que potencialmente ahorraría tiempo y recursos.
# 
# Basándonos en los análisis y preprocesamiento de datos ya realizados, los siguientes pasos son:
# 
# 1. Normalizar o estandarizar las características para asegurar que todas tengan igual importancia en el modelo.  
# Por ejemplo, con los datos encontrados, vimos que la mayoría de las variables tenían una correlación muy baja con la variable objetivo,  
# por lo que es probable que no sean muy buenas predictoras de esta.
# 
# 2. Dividir los datos en conjuntos de entrenamiento y prueba (por ejemplo, 80% para entrenamiento y 20% para prueba).
# 
# 3. Aplicar alguna técnica de selección de características para identificar las variables más importantes que influyen en la calidad del vino.  
# Por ejemplo, [sklearn.feature_selection](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection)
# 
# 4. Seleccionar algoritmos de aprendizaje automático apropiados como Regresión Lineal, Árboles de Decisión, Random Forest, o Gradient Boosting.  
# (es recomendado utilizar varios y comparar los resultados)
# 
# 5. Evaluar el rendimiento del modelo utilizando métricas como MAE, RMSE, y R².
# 
# 6. Implementar un sistema de toma de muestras para alimentar el modelo y obtener nuevas predicciones.

# ### Desafios
# - Datos:
#     - **Calidad de Datos**: Dado que existen métodos de manejo de duplicados y outliers, existe la posibilidad de que los datos se encuentren sesgados,  
#     por lo que podría ser necesario abordar este sesgo antes de generar el modelo.
#     
#     - **Desequilibrio de Clases**: La distribucion de la calidad del vino esta desequilibrada, con muchas muestras en las categorias 5, 6,  
#     y  pocas en otras, lo que puede afectar la capacidad del modelo para predecir correctamente todas las clases.
#     
#     - **Sobreajuste**: El modelo puede ajustarse demasiado a los datos de entrenamiento y no generalizar bien a datos nuevos.
# 
# - Practicos:
#     - **Integración con Sistemas Existentes**: Integrar el modelo con los sistemas de gestión y producción de la viña, puede ser más complicado de lo esperado.
# 
#     - **Mantenimiento y Actualización del Modelo**: Será necesario crear un sistema para mantener el modelo monitoreado y actualizado conforme cambien las condiciones de producción.
# 
#     - **Costos de Implementación**: Inversión inicial en infraestructura y capacitación.
