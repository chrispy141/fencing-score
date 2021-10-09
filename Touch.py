import requests


url = 'http://127.0.0.1:8008/hit'
increment = {'id': 1}
decrement = {'id': 1}
reset = {'id': 1}


def touch(id):
   postJson = {'id' : id, 'value' : 1}
   try:
      x = requests.post(url, json = postJson)
   except:
      print("http post failed") 

def removeTouch(id):
   postJson = {'id' : id, 'value' : -2}
   try:
      x = requests.post(url, json = postJson)
   except:
      print("http post failed") 

def reset(id):
   postJson = {'id' : id, 'value' : 0}
   try:
      x = requests.post(url, json = postJson)
   except:
      print("http post failed") 
