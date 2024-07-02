import requests
from django.core.files.base import ContentFile


import os, sys    

current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path[:current_path.find(os.path.dirname(__file__))]
sys.path.append(current_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cer3.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from backend.models import Pokemon

def obtener_datos_de_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except ValueError:
            print("Error: No se pudo decodificar el JSON")
    else:
        print(f"Error: La petición HTTP falló con el código {response.status_code}")

def obtener_descripcion_pokemon(species_url):
    response = requests.get(species_url)
    if response.status_code == 200:
        try:
            data = response.json()
            
            for entry in data['flavor_text_entries']:
                if entry['language']['name'] == 'es':
                    return entry['flavor_text']
            
            for entry in data['flavor_text_entries']:
                return entry['flavor_text']
            
            print("Error: No se encontró descripción válida del Pokémon")
        
        except (ValueError, KeyError):
            print("Error: No se pudo obtener la descripción del Pokémon")
    
    else:
        print(f"Error: La petición HTTP falló con el código {response.status_code}")

# URL de la API
url_api = 'https://pokeapi.co/api/v2/pokemon?limit=151'

def obtener_y_almacenar_datos():   
    datos_recibidos = obtener_datos_de_api(url_api)
    pokemons = datos_recibidos['results'] 
    
    for pokemon in pokemons:
        name = pokemon['name']
        poke_data = obtener_datos_de_api(pokemon['url'])
        pokedex_number = poke_data['id']
        primary_type = poke_data['types'][0]['type']['name']
        secondary_type = None
        if len(poke_data['types']) > 1:
            secondary_type = poke_data['types'][1]['type']['name']
        
        species_url = poke_data['species']['url']
        description = obtener_descripcion_pokemon(species_url)
        
        front_image_url = poke_data['sprites']['other']['showdown']['front_default']

        poke_db, _ = Pokemon.objects.get_or_create(
            name=name,
            pokedex_number=pokedex_number,
            primary_type=primary_type,
            secondary_type=secondary_type,
            image_url=front_image_url,
            description=description
        )

        print(poke_db)

obtener_y_almacenar_datos()