import requests


iss = requests.get("http://api.open-notify.org/iss-now.json/").json()
print('iss is at')
print("latitude: ",iss.get("iss_position").get("latitude"))
print("longitude: ",iss.get("iss_position").get("longitude"))
print("as of :",iss.get("timestamp"))