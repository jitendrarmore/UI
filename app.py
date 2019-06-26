#!/usr/bin/env python
# coding=utf-8
from flask import request
from flask import Flask
import os
import json
from flask_httpauth import HTTPBasicAuth
from flask import json

app = Flask(__name__, static_url_path="/find/api")
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
  if username == 'jmore':
    return 'python'
  return None

@app.route('/find/api', methods=['POST'])
@auth.login_required
def create_task():
  if request.headers['Content-Type'] == 'text/plain':
    return "Text Message: " + request.data

  elif request.headers['Content-Type'] == 'application/json':
    a = request.json
    while (type(a) is dict):
    	a = a.values()[0]
    if str(a[0]) == 'p':
	return str(a)
    else:
	return '["'+ str(a[0])+'"]'
    return str(a)


if __name__ == '__main__':
  app.run(debug=True)
