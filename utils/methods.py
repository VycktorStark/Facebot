#-*- coding: utf-8 -*-
from utils.config import TOKEN
from utils.requests import request_post
import sys, json, os, utils.methods
def log(message):
    print(message)
    sys.stdout.flush()
def sendRequest(data):
  params = {"access_token": TOKEN}
  headers = {"Content-Type": "application/json"}
  request_post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=json.dumps(data))
def sendMessage(chat_id, text):
    data = sendRequest({"recipient": {"id": chat_id},"message": {"text": text}})
    return data