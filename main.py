import requests

URL_BASE = "https://rickandmortyapi.com/api"
RESOURCES = {
    "characters": f"{URL_BASE}/character",
    "locations": f"{URL_BASE}/location",
    "episodes": f"{URL_BASE}/episode"
}


def search_character(name):
    respuesta = requests.get(RESOURCES['characters'], {"name": name})
    respuesta_json = respuesta.json()
    return respuesta_json['results'][0]


def get_location(character):
    location_url = character['location']['url']
    location = requests.get(location_url).json()
    return location


def get_episodes(character):
    episode_url = character['episode'][0]
    episodes = requests.get(episode_url).json()
    return episodes


def get_input():
    print("Introduzca un nombre de personaje:")
    character_name = input()
    print(f"El personaje seleccionado es: , {character_name}")
    return character_name


if __name__ == "__main__":
    character_name = get_input()
    character = search_character(character_name)
    location = get_location(character)
    episodes = get_episodes(character)

    print(f" Character info -> \"species\": {character['species']}, \"type\": {character['type']}")
    print(f" Location/s info -> \"name\": {location['name']}, \"type\": {location['type']}, \"dimension\": {location['dimension']}, \"population\":{len(location['residents'])}")
    print(f" Episode/s info -> \"episode_name\": {episodes['name']}, \"episode_id\": {episodes['episode']}, \"character_count\": {len(episodes['characters'])}")
