import requests
import os
import socket
import struct
import sys

increment = {'id': 1}
decrement = {'id': 1}
reset = {'id': 1}


def touch(url, id):
   postJson = {'id' : id, 'value' : 1}
   try:
      x = requests.post(url, json = postJson)
   except:
      print("http post failed") 

def removeTouch(url, id):
   postJson = {'id' : id, 'value' : -2}
   try:
      x = requests.post(url, json = postJson)
   except:
      print("http post failed") 

def reset(url, id):
   postJson = {'id' : id, 'value' : 0}
   try:
      x = requests.post(url, json = postJson)
   except:
      print("http post failed") 

def scream():
   os.system("afplay scream.wav")

def getMyIP():
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect(("8.8.8.8", 80))
   retval = s.getsockname()[0]
   s.close()
   return retval

def getServerIP():
   multicast_group = '224.3.29.71'
   server_address = ('', 10000)
   
   # Create the socket
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   
   # Bind to the server address
   sock.bind(server_address)
   
   group = socket.inet_aton(multicast_group)
   mreq = struct.pack('4sL', group, socket.INADDR_ANY)
   sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
   
   # Receive/respond loop
   while True:
       print('\nwaiting to receive message')
       data, address = sock.recvfrom(1024)
       return data.decode('utf-8')

def sendServerIP():
   message = getMyIP().encode('utf-8')
   multicast_group = ('224.3.29.71', 10000)
   
   # Create the datagram socket
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   
   # Set a timeout so the socket does not block indefinitely when trying
   # to receive data.
   #sock.settimeout(0.2)
   try:
  
      # Send data to the multicast group
      print('sending "%s"' % message)
      sent = sock.sendto(message, multicast_group)
   
   finally:
      print('closing socket')
      sock.close()

def getUrl():
   url = "http://"+getServerIP() + ":8008/hit"
   return url
