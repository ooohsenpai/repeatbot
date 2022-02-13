from flask import Flask, request
import requests
import os

app = Flask(__name__)

def send_message(chat_id, text):
    method = "sendMessage"
    token = os.environ['TG_API_KEY']
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.route("/telegram", methods=['POST'])
def receive_update():
    if request.method == "POST":
        chat_id = request.json["message"]["chat"]["id"]
        text = request.json["message"]["text"]
        send_message(chat_id, text)