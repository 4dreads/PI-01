# PI-01
# Sistema personalizado de recomendación de juegos

# Introducción:
El sistema de recomendación de juegos es una aplicación web que sugiere juegos según las preferencias del usuario. Utiliza un conjunto de datos de juegos de Steam y reseñas de usuarios para generar recomendaciones de juegos personalizadas. El sistema utiliza procesamiento del lenguaje natural (NLP) para extraer funciones de los títulos de juegos y un algoritmo de filtrado colaborativo para generar recomendaciones.

# Preparación de datos:
El conjunto de datos utilizado en este proyecto consta de dos archivos steam_games.gz.jsony user_reviews.gz.json. El primer archivo contiene información sobre los juegos, incluido el título, el desarrollador y el género. El segundo archivo contiene reseñas de usuarios, incluida la identificación del usuario, la identificación del juego y la calificación.

El código primero carga los datos de los archivos y normaliza los valores de cadena en el conjunto de datos. Luego vectoriza los títulos de los juegos usando TfidfVectorizer y calcula la similitud del coseno entre los títulos de los juegos.

# Sistema de recomendación:
El sistema de recomendación consta de dos funciones: recomendacion_juegoy recomendacion_usuario. La recomendacion_juegofunción toma una ID de juego como entrada y devuelve los 5 juegos más similares según la similitud del coseno. La recomendacion_usuariofunción toma una identificación de usuario como entrada y devuelve los 10 juegos más recomendados según el historial de reseñas del usuario.

Para generar recomendaciones para un usuario, el sistema primero carga el historial de revisiones del usuario desde el user_reviews.gz.jsonarchivo. Luego filtra las reseñas del usuario según la identificación del usuario y crea un conjunto de prueba para el usuario. Luego, el sistema genera recomendaciones para el usuario utilizando el KNNWithMeansalgoritmo de la biblioteca Surprise.

# Implementación:
El sistema de recomendación se implementa utilizando FastAPI, un marco web moderno, rápido (de alto rendimiento) para crear API con Python 3.6+ basado en sugerencias de tipo Python estándar.

En general, este proyecto demuestra el potencial de los sistemas de recomendación para brindar recomendaciones personalizadas a los usuarios y mejorar su experiencia en línea. El sistema se puede mejorar aún más incorporando más fuentes de datos, como datos demográficos de los usuarios y datos de juego, y utilizando algoritmos de recomendación más sofisticados.

# Código:

import gzip

import json

import pandas as pd

from fastapi import FastAPI

from pydantic import BaseModel

from typing import List, Dict, Tuple, List

from collections import Counter

from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import TfidfVectorizer

from surprise import Dataset, Reader, KNNWithMeans

from surprise.model_selection import cross_validate

app = FastAPI()

# Cargar los datos de juegos
with gzip.open('steam_games.gz.json', 'rt') as f:
    steam_games = json.load(f)

# Convertir los datos de juegos a un DataFrame de Pandas
data = pd.json_normalize(steam_games)

# Normalizar los valores de cadena en el dataset
data['title'] = data['title'].apply(normalizar_string)
data['developer'] = data['developer'].apply(normalizar_string)

# Vectorizar los datos de juegos
vectorizer = TfidfVectorizer(stop_words='english')
juegos_vectorizados = vectorizer.fit_transform(data['title'])

# Calcular la similitud del coseno entre los juegos
similitud_coseno = cosine_similarity(juegos_vectorizados)

# Función para normalizar los valores de cadena
def normalizar_string(s: str) -> str:
    return " ".join(s.lower().split())

# Función para obtener las recomendaciones de un juego
def recomendacion_juego(id_juego: int) -> Recomendacion:
    # Encontrar el índice del juego en el dataset
    indice
