import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'мой токен'
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '5024'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', 'Dobra Kusok'), ('id', '5024')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value