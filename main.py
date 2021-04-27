import requests


def intelligence_hero(name):
    intelligence_dict = {}
    for hero in name:
        url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        resp = requests.get(url)
        results = resp.json()
        for key in results['results']:
            intelligence_dict[hero] = key['powerstats']['intelligence']
    print(max(intelligence_dict))


heroes = ['Hulk', 'Captain America', 'Thanos']

intelligence_hero(heroes)
