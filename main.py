import requests

res_object = requests.get("https://api.adviceslip.com/advice")
response = res_object.json()
print(response)
print(response["slip"]["advice"])