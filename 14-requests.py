import requests

response = requests.get('https://ucm.es')

print(response.text)
