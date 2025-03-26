import requests

#Realizar una búsqueda de cartas por nombre
url = "https://api.scryfall.com/cards/search"
params = {"q": "nombre:Black Lotus"}
response = requests.get(url, params=params)

#Imprimir la información de la carta
if response.status_code == 200:
    data = response.json()
    print(data["data"][0]["name"])
    print(data["data"][0]["text"])
else:
    print("Error al obtener la carta")