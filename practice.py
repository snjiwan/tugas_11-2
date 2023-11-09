import requests

api_key = '82bbe5af-fb0f-4ad4-88ce-9cbb498cf245'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definition = res.json()

for definition in definition:
    print(definition)