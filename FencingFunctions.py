import requests


url = 'http://10.252.205.112:8008/hit'
increment = {'id': 1}
decrement = {'id': 1}
reset = {'id': 1}


def touch(id):
   postJson = {'id' : id, 'value' : 1}
   x = requests.post(url, json = postJson)
  

def removeTouch(id):
   postJson = {'id' : id, 'value' : -1}
   x = requests.post(url, json = postJson)

def reset(id):
   postJson = {'id' : id, 'value' : 0}
   x = requests.post(url, json = postJson)
