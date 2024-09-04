import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'мой токен'
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "kusokdobra",
    "photo_id": 333
}
body_rename = {
    "pokemon_id": "67618",
    "name": "chumbawumba",
    "photo_id": 456
}
body_catch = {
    "pokemon_id": "67618"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
response_2 = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
response_3 = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)

print(response.text, response_2.text, response_3.text)