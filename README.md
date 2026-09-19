# Analisis de pasajeros del Titanic

## Descripcion

Este proyecto realiza limpieza, preprocesamiento, analisis exploratorio y visualizacion de datos utilizando el dataset Titanic de Kaggle.

## Dataset

Nombre: Titanic - Machine Learning from Disaster

Fuente: Kaggle

Archivo utilizado: `data/train.csv`

El dataset contiene informacion de pasajeros del Titanic, incluyendo edad, sexo, clase, tarifa y supervivencia.

## Objetivo

Analizar algunas caracteristicas de los pasajeros para identificar diferencias relacionadas con la supervivencia.

## Requisitos

Se requiere Python y las dependencias incluidas en el archivo `requirements.txt`.

## Instalacion

Clonar el repositorio:

```bash
git clone https://github.com/Coquito2707/titanic-data-project.git
```

Entrar a la carpeta del proyecto:
```bash
cd titanic-data-project
```
Crear un entorno virtual:
```bash
python -m venv .venv
```
Activar entorno virtual en windows:
```bash
.venv\Scripts\activate
```
Instalar las dependencias:
```bash
pip install -r requirements.txt
```
## Ejecucion 
Ejecutar el proyecto con 
```bash
python src/analysis.py
```
## Analisis realizados
- Porcentaje general de supervivencia.
- Supervivencia por sexo.
- Supervivencia por clase.
- Supervivencia por grupo de edad.

## Resultados y conclusiones

Aproximadamente el 38.38% de los pasajeros sobrevivio.

Las mujeres presentaron una proporcion de supervivencia mayor que los hombres.

Los pasajeros de primera clase tuvieron una mayor supervivencia que los pasajeros de segunda y tercera clase.

Los ninos presentaron la mayor proporcion de supervivencia entre los grupos de edad analizados.