import sys
import requests
from urllib.parse import urlencode

API_DEV_KEY = "8fc27602ffa62fa1e34e04417b949cda"


def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Getting information for {pokemon_name}...success")
        return response.json()
    else:
        print(f"Getting information for {pokemon_name}...failure")
        print(f"Response code: {response.status_code} ({response.reason})")
        return None
def create_paste(TITLE, BODY , EXPIRATION, PUBLIC):
    api_url = "https://pastebin.com/api/api_post.php"
    API_PASTE_FORMAT = "text"
    params = {
        "api_dev_key": API_DEV_KEY,
        "api_option": "paste",
        "api_paste_name": TITLE,
        "api_paste_format": API_PASTE_FORMAT,
        "api_paste_code": BODY ,
        "api_paste_expire_date": EXPIRATION,
        "api_paste_private": PUBLIC,
        
    }
    response = requests.post(api_url, data=params)
    if response.status_code == 200 and 'pastebin.com/' in response.text:
        print("Posting new paste to PasteBin...success")
        print(response.text)
        return
    else:
        print("Posting new paste to PasteBin...failure")
        return None
def get_pokemon_name():
    if len(sys.argv) == 2:
        return sys.argv[1]
    else:
        print("Usage: python pokemon_paste.py <pokemon_name>")
        sys.exit()


def construct_paste(pokemon_info):
    name = pokemon_info["name"].capitalize()
    abilities = "\n".join(
        [ability["ability"]["name"] for ability in pokemon_info["abilities"]])
    TITLE = f"{name}'s Abilities"
    BODY = abilities
    return (TITLE, BODY)
def main():
    paste_url
    pokemon_name = get_pokemon_name()
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info is not None:
        TITLE, BODY = construct_paste(pokemon_info)
        PUBLIC = 0
        EXPIRATION = '1M'
        paste_url = create_paste(TITLE, BODY, EXPIRATION, PUBLIC)

if   __name__ == "_main_":
     main()

