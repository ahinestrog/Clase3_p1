import pandas as pd
import json

# Read the CSV file
df = pd.read_csv('movies_initial.csv')

# Guarda el DataFrame en un archivo JSON

df.to_json('movies.json', orient='records')

with open('movies.json', 'r') as file:
    movies = json.load(file)

for i in range(100):
    movies = movies[i]
    print(movies)
    break