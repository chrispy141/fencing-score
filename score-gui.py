from flask import Flask, jsonify, request

from threading import Thread
import PySimpleGUI as sg
import time
app = Flask(__name__)

scores = {}
keys = {}
keylist = ['-F1-', '-F2-']
numFencers = 0;
layout = [[sg.Text("No Fencer yet", key='-F1-' )],[sg.Text("No Fencer Yet", key='-F2-')],[sg.Button("OK")]]
window = sg.Window("Goats rock!", layout)


def update_scores():
   for id in scores.keys():
      window[keys[id]].update(id + ":" + str(scores[id]))


@app.route('/hit', methods=['POST'])
def add_hit():
  global numFencers
  recv = request.get_json()
  id = recv["id"]
  if id in scores.keys(): 
     
     scores[id] = scores[id] + recv["value"]
     if recv["value"] == 0:
        scores[id] = 0 
  else:
     if numFencers < 2:
        print("New Contender! " + id)
        scores[id] = recv["value"]
        keys[id] = keylist[numFencers]
        numFencers = numFencers + 1
  return '', 204


if __name__ == '__main__':
   kwargs={'host':'0.0.0.0', 'port':8008}
   print("Before Thread")
   Thread(target=app.run, daemon=True, kwargs=kwargs).start()
   print("After Thread")
   while True:
      event, values = window.read(timeout=500)
      if event == "OK":
         break
      if event == sg.WIN_CLOSED:
         break
      update_scores()
