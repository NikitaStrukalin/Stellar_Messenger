import requests

url = "https://stellar-service-dt2w.onrender.com"

json = {
   "username" : "Nikita"
}

requests.post(url=url, json=json)
