from flask import Flask, jsonify, request
from tkinter import *
from threading import Thread

from FencingFunctions import *

import PySimpleGUI as sg
import time
app = Flask(__name__)

scores = {}
keys = {}
keylist = ['-F1-', '-F2-']
numFencers = 0;


layout = [[sg.Text("No Fencer yet",size=(30,5), key='-F1-', font=('Georgia 20') )],[sg.Text("No Fencer Yet",size=(30,5), key='-F2-', font=('Georgia 20'))],[sg.Button("Reset")]]
window = sg.Window("Goats rock!", layout)

def reset_scores():
   for id in scores.keys():
      scores[id] = 0
 
def update_scores():
   for id in scores.keys():
      window[keys[id]].update(id + ":  " + str(scores[id]))


@app.route('/hit', methods=['POST'])
def add_hit():
  global numFencers
  recv = request.get_json()
  id = recv["id"]
  if id in scores.keys(): 
     
     scores[id] = scores[id] + recv["value"]
     if recv["value"] == 0:
        scores[id] = 0 
     if recv["value"] > 0:
        scream()
  else:
     if numFencers < 2:
        print("New Contender! " + id)
        scores[id] = recv["value"]
        keys[id] = keylist[numFencers]
        numFencers = numFencers + 1
        if recv["value"] > 0:
           scream()
  return '', 204


if __name__ == '__main__':
   kwargs={'host':'0.0.0.0', 'port':8008}
   print("Before Thread")
   Thread(target=app.run, daemon=True, kwargs=kwargs).start()
   print("After Thread")
   while True:
      event, values = window.read(timeout=500)
      if event == "Reset":
         reset_scores()
      if event == sg.WIN_CLOSED:
         break
      update_scores()
