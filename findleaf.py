#!/usr/local/bin/python3

import os
import json

path = os.path.abspath('a.json')
with open(path) as f:
  a = json.loads(file.read(f) )
  #print(type(a))

#Defining a fuction where type if the dictionary is true
def printLeaf(a):
  while (type(a) is dict):
    a = a.values()[0]
  print(str(a))

printLeaf(a)
