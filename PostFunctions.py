import requests

url = 'http://localhost:8008/hit'
myobj = {'id': 'goats!'}

x = requests.post(url, json = myobj)

print(x.text)
