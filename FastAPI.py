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

with gzip.open('steam_games.gz.json', 'rt') as f:
    steam_games = json.load(f)

data = pd.json_normalize(steam_games)

data['title'] = data['title'].apply(normalizar_string)
data['developer'] = data['developer'].apply(normalizar_string)

vectorizer = TfidfVectorizer(stop_words='english')
juegos_vectorizados = vectorizer.fit_transform(data['title'])

similitud_coseno = cosine_similarity(juegos_vectorizados)

def normalizar_string(s: str) -> str:
    return " ".join(s.lower().split())

def recomendacion_juego(id_juego: int) -> Recomendacion:
    indice_juego = data[data['id'] == id_juego].index[0]

    similitudes = list(enumerate(similitud_coseno[indice_juego]))

    similitudes_ordenadas = sorted(similitudes, key=lambda x: x[1], reverse=True)

    recomendaciones = [data.iloc[indice]['title'] for indice, similitud in similitudes_ordenadas[1:6]]
    
    return Recomendacion(juegos=recomendaciones)

def recomendacion_usuario(id_usuario: str) -> RecomendacionUsuario:
    id_usuario = normalizar_string(id_usuario)
    
    with gzip.open('user_reviews.gz.json', 'rt') as f:
        user_reviews = json.load(f)

    with gzip.open('user_items.gz.json', 'rt') as f:
        user_items = json.load(f)

    usuario_data = [r for r in user_reviews if r['user_id'] == id_usuario]
    items_usuario = [i for i in user_items if i['user_id'] == id_usuario]

    usuario_prueba = Dataset.load_from_folds([{'user_id': id_usuario, 'item_id': [i['


  
