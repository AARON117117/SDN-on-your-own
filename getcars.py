import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint



USER = "devnetuser"
PASS = "Cisco123!"
URL = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"




headers = {'Content-Type': 'application/json'}


response = requests.post(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)


token = response.json()['Token']


Volvo = "https://sandboxdnac.cisco.com/dna/intent/api/v1/site"

getHeader = {'Accept': 'application/json', 'X-auth-token': token}

getResponse = requests.get(Volvo, headers=getHeader, verify=False)


CorvetteJSON = getResponse.json()

#prints CorvetteJSON to the screen

pprint(CorvetteJSON)



