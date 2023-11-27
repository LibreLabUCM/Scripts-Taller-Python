import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/zapdos')

print(response.json())
