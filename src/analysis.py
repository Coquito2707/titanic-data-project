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