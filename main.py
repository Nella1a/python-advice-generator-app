import requests

res_object = requests.get("https://api.adviceslip.com/advice")
response = res_object.json()
#print(response)
print("****** Get random advice ******")
print(f'#{response["slip"]["id"]}: {response["slip"]["advice"]}"\n')

print("****** Search advice ******")
keyword = input("Search term: ")
res_object = requests.get(f'https://api.adviceslip.com/advice/search/{keyword}')
response = res_object.json()
#print(response)

if "message" in response:
     print(response["message"]["text"])
else:
    print(f'result(s): {response["total_results"]}')
    for advice in response["slips"]:
      print(f'#{advice["id"]}: {advice["advice"]}')
