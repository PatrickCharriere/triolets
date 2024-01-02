import requests
import ast

standSize = 3
minValue = 0
maxValue = 15
jokersQty = 2
randomNames = ["Toto", "Titi"]
def getRandomNames():
    gender = 'neutral'
    api_url = 'https://api.api-ninjas.com/v1/babynames?gender={}'.format(gender)
    response = requests.get(api_url, headers={'X-Api-Key': 'DcWDB9DFiqaEYjSvCvcI2g==AiXGFX2342TLEqC8'})
    if response.status_code == requests.codes.ok:
        names = ast.literal_eval(response.text)
        randomNames[0] = names[0]
        randomNames[1] = names[1]
    else:
        print("Error:", response.status_code, response.text)


getRandomNames()