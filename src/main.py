import requests
import pandas as pd
from pokemon_model import Pokemon
from pokemon_model import Pokemon, FirePokemon, GroundPokemon, BugPokemon

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")

data = response.json()

pokemon_list = data["results"]

pokemon_objects = [Pokemon(p['name'], detail_url = p['url']) for p in pokemon_list]

def get_main_type(detail_url):
    response = requests.get(detail_url)
    data = response.json()
    types = [t['type']['name'] for t in data['types']]
    return types[0]  

pokemon_objects_with_types = []

for p in pokemon_objects:

    main_type = get_main_type(p.detail_url)
    if main_type == "fire":
        pokemon_objects_with_types.append(FirePokemon(p.name, p.detail_url))
    elif main_type == "ground":
        pokemon_objects_with_types.append(GroundPokemon(p.name, p.detail_url))
    elif main_type == "bug":
        pokemon_objects_with_types.append(BugPokemon(p.name, p.detail_url))
    else:
        pokemon_objects_with_types.append(Pokemon(p.name, p.detail_url))

df = pd.DataFrame([{
    "name": p.name, 
    "url": p.detail_url,
    "type": "fire" if isinstance(p, FirePokemon)
           else "ground" if isinstance(p, GroundPokemon)
           else "bug" if isinstance(p, BugPokemon)
           else "other"
    } for p in pokemon_objects_with_types])


df["name"] = df["name"].str.capitalize()


df.to_csv("pokemon_data.csv", index=False)
