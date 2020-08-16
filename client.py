import json
import requests


test_sym = ['continuous_sneezing','shivering','chills','cough','chest_pain']
padding = ['not_needed' for i in range(12)]
for m in padding:
    test_sym.append(m)

arg_dict = {'symptoms':test_sym}

base_url = 'http://localhost:5000/api/mediserve/v1/'

url = base_url + json.dumps(arg_dict)


response_raw = requests.get(url)
response = json.loads(response_raw.text)
print(response)
print()
print(url)