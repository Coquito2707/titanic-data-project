import pandas as pd

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