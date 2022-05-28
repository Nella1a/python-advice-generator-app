import requests

res_object = requests.get("https://api.adviceslip.com/advice")
response = res_object.json()
#print(response)

print(f'****** ADVICE {response["slip"]["id"]} ******')
print(f'"{response["slip"]["advice"]}"\n')
