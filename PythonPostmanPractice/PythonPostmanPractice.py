import requests
import json

url = "https://library-api.postmanlabs.com/books"
params = {"author": "Harper Lee"}  # Define query parameters here
#params = {"ID Year": 2017}
response = requests.get(url, params=params)  # Pass params to requests.get()


print(json.dumps(response.json(), indent=4))

if response.status_code == 200:
    population = None
    for item in response.json():
        if item.get("ID Year") == params["ID Year"]:
            population = item.get("ID Nation")
            break
    if population:
        print("Population found:")
        print(json.dumps(population, indent=4))
    else:
        print("Population with the specified ID Year not found.")
else:
    print("Failed to fetch population. Status code:", response.status_code)