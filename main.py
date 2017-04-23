#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, request
import random, json, re, os, requests
from utils.config import SENHA, debug, AiApi
from utils.methods import sendMessage, log
from urllib.request import urlopen
app = Flask(__name__)
@app.route('/', methods=['GET'])
def verify(): #Token verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == SENHA:
            return "Missing check token matching", 403
        return request.args["hub.challenge"], 200
    return "Check token match - OK", 200


@app.route('/', methods=['POST'])
def body():
    data = request.get_json()
    data = data['entry'][0]
    if data.get('messaging') and data['messaging'][0].get('message'):
      result = urlopen(AiApi.format(host="", BotID="", msg=data['messaging'][0]['message']['text'].encode('utf8'))).read()
      sendMessage(data['messaging'][0]["sender"]['id'], result.decode('utf8'))
    return "ok", 200

if __name__ == '__main__':
    app.run(debug=True,port=3000,host='0.0.0.0')