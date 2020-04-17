import requests

def searchHero(key, name):
    response = requests.get('https://superheroapi.com/api/{0}/search/{1}'.format(key, name))
    return response.text