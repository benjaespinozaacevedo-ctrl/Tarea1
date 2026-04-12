import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
print("\nDimensiones del dataset:")
print(df.shape)
print("\nValores faltantes por columna:")
print(df.isnull().sum())
print("\nEstadísticas descriptivas:")
print(df.describe())
print("\nSupervivencia:")   #personas que sobreviven
print(df["survived"].value_counts())
print(" sexo:")
print(df["sex"].value_counts()) 
plt.figure(figsize=(6,4))
df["survived"].value_counts().plot(kind="bar")
plt.title("Cantidad de pasajeros que sobrevivieron")
plt.xlabel("Survived ")
plt.ylabel("Cantidad")
plt.show()

plt.figure(figsize=(6,4))
df["age"].dropna().plot(kind="hist", bins=20)
plt.title("Distribución de edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()
plt.figure(figsize=(6,4))
df["pclass"].value_counts().sort_index().plot(kind="bar")
plt.title("Cantidad de pasajeros por clase")
plt.xlabel("Clase")
plt.ylabel("Cantidad")
plt.show()

plt.figure(figsize=(6,4))
df["age"].dropna().plot(kind="hist", bins=20)
plt.title("Distribución de edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()
print("\nCantidad de pasajeros por clase:")
print(df["pclass"].value_counts().sort_index())

df["pclass"].value_counts().sort_index().plot(kind="bar", figsize=(6,4))
plt.title("Cantidad de pasajeros por clase")
plt.xlabel("Clase")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.show()
tabla_sexo_supervivencia = pd.crosstab(df["sex"], df["survived"])
tabla_sexo_supervivencia.columns = ["Murieron", "Sobrevivieron"]

print("\nSupervivencia y muerte según sexo:")
print(tabla_sexo_supervivencia)

tabla_sexo_supervivencia.plot(kind="bar", figsize=(6,4))
plt.title("Supervivencia y muerte según sexo")
plt.xlabel("Sexo")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.show()
## A partir de los gráficos y del análisis realizado, se puede observar que el dataset Titanic presenta diferencias importantes
#  entre los pasajeros. La supervivencia no fue pareja, ya que murieron más personas de las que sobrevivieron. Además, la distribución 
# de edades muestra que viajaban personas de distintas etapas de la vida, y la cantidad de pasajeros por clase evidencia que no todos 
# tenían las mismas condiciones a bordo. Finalmente, al comparar sexo con supervivencia, se aprecia una diferencia clara entre
#  hombres y mujeres, lo que sugiere que esta variable influyó en las probabilidades de sobrevivir. En conjunto, los gráficos
#  permiten entender de forma simple cómo estaban distribuidos los pasajeros y qué factores pudieron relacionarse con la supervivencia.