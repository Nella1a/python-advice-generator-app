import requests

res_object = requests.get("https://api.adviceslip.com/advice")
response = res_object.json()
#print(response)
print("Get random advice: ")
print(f'****** ADVICE {response["slip"]["id"]} ******')
print(f'"{response["slip"]["advice"]}"\n')

print("Searching advice: ")
keyword = input("Keyword: ")
res_object = requests.get(f'https://api.adviceslip.com/advice/search/{keyword}')
response = res_object.json()
#print(response)

print(f'results: {response["total_results"]}')
if len(response["slips"]) > 0:
  for advice in response["slips"]:
    print(f'#{advice["id"]}: {advice["advice"]}')