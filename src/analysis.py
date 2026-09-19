import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/train.csv")

print("Primeras filas del dataset:")
print(df.head())

print("\nNumero de pasajeros:")
print(df.shape[0])

print("\nNumero de columnas:")
print(df.shape[1])

print("\nVariables disponibles:")
print(df.columns.tolist())

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores faltantes:")
print(df.isnull().sum())

print("\nRegistros duplicados:")
print(df.duplicated().sum())

print("\nEstadisticas descriptivas:")
print(df.describe())

print("\nValores faltantes en Age:")
print(df["Age"].isnull().sum())

print("\nMedia de Age:")
print(df["Age"].mean())

print("\nMediana de Age:")
print(df["Age"].median())

df["Age"] = df["Age"].fillna(df["Age"].median())

print("\nValores faltantes en Age despues de la limpieza:")
print(df["Age"].isnull().sum())

print("\nValores faltantes en Cabin:")
print(df["Cabin"].isnull().sum())

print("\nPorcentaje de valores faltantes en Cabin:")
print(df["Cabin"].isnull().mean() * 100)

df = df.drop(columns=["Cabin"])

print("\nColumnas despues de eliminar Cabin:")
print(df.columns.tolist())

print("\nValores faltantes en Embarked:")
print(df["Embarked"].isnull().sum())

print("\nValores de Embarked:")
print(df["Embarked"].value_counts())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\nValores faltantes en Embarked despues de la limpieza:")
print(df["Embarked"].isnull().sum())

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

def clasificar_edad(edad):
    if edad < 13:
        return "Nino"
    elif edad < 18:
        return "Joven"
    elif edad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"

df["AgeGroup"] = df["Age"].apply(clasificar_edad)

print("\nNuevas variables:")
print(df[["FamilySize", "AgeGroup"]].head())
porcentaje_supervivencia = df["Survived"].mean() * 100

print("\nPorcentaje de pasajeros que sobrevivio:")
print(round(porcentaje_supervivencia, 2), "%")

supervivencia_sexo = df.groupby("Sex")["Survived"].mean() * 100

print("\nSupervivencia por sexo:")
print(supervivencia_sexo.round(2))

supervivencia_clase = df.groupby("Pclass")["Survived"].mean() * 100

print("\nSupervivencia por clase:")
print(supervivencia_clase.round(2))

supervivencia_edad = df.groupby("AgeGroup")["Survived"].mean() * 100

print("\nSupervivencia por grupo de edad:")
print(supervivencia_edad.round(2))

supervivencia_sexo.plot(kind="bar")

plt.title("Supervivencia por sexo")
plt.xlabel("Sexo")
plt.ylabel("Porcentaje de supervivencia")
plt.tight_layout()

plt.savefig("outputs/resultados/supervivencia_sexo.png")
plt.close()

supervivencia_clase.plot(kind="bar")

plt.title("Supervivencia por clase")
plt.xlabel("Clase del pasajero")
plt.ylabel("Porcentaje de supervivencia")
plt.tight_layout()

plt.savefig("outputs/resultados/supervivencia_clase.png")
plt.close()

supervivencia_edad.plot(kind="bar")

plt.title("Supervivencia por grupo de edad")
plt.xlabel("Grupo de edad")
plt.ylabel("Porcentaje de supervivencia")
plt.tight_layout()

plt.savefig("outputs/resultados/supervivencia_edad.png")
plt.close()

print("\nConclusiones:")
print("1. Aproximadamente el 38.38% de los pasajeros sobrevivio.")
print("2. Las mujeres tuvieron una supervivencia mucho mayor que los hombres.")
print("3. Los pasajeros de primera clase tuvieron mayor supervivencia que los de segunda y tercera clase.")
print("4. Los ninos presentaron la mayor supervivencia entre los grupos de edad analizados.")