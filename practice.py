import requests

api_key = 'c2597462-3f36-47d2-ba41-282ea321d309'
word = 'banana'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)