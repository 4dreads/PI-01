import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from surprise import Dataset, Reader, KNNWithMeans
from surprise.model_selection import cross_validate

data = pd.read_csv('juegos.csv')

print("Primeras filas de los datos:")
print(data.head())

print("\nEstadísticas descriptivas de los datos:")
print(data.describe())

print("\nFrecuencia de cada género:")
print(data['genero'].value_counts())

print("\nFrecuencia de cada plataforma:")
print(data['plataforma'].value_counts())

print("\nFrecuencia de cada clasificación de edad:")
print(data['clasificacion_edad'].value_counts())

print("\nFrecuencia de cada desarrollador:")
print(data['desarrollador'].value_counts())

print("\nFrecuencia de cada editor:")
print(data['editor'].value_counts())

print("\nFrecuencia de cada tipo de relación con el usuario:")
print(data['relacion_usuario'].value_counts())

print("\nFrecuencia de cada tipo de sentimiento:")
print(data['sentiment_analysis'].value_counts())

vectorizer = TfidfVectorizer(stop_words='english')
juegos_vectorizados = vectorizer.fit_transform(data['titulo'])

similitud_coseno = cosine_similarity(juegos_vectorizados)

def recomendacion_juego(id_juego):
    indice_juego = data[data['id'] == id_juego].index[0]

    similitudes = list(enumerate(similitud_coseno[indice_juego]))

    similitudes_ordenadas = sorted(similitudes, key=lambda x: x[1], reverse=True)

    recomendaciones = [data.iloc[indice]['titulo'] for indice, similitud in similitudes_ordenadas[1:6]]
    
    return recomendaciones

print("\nRecomendaciones para el juego con ID 1:")
print(recomendacion_juego(1))

lector = Reader(rating_scale=(1, 5))

data_prueba = Dataset.load_from_df(data[['usuario', 'juego', 'clasificacion']], lector)

modelo = KNNWithMeans(k=5
