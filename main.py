from flask import Flask, request
import requests
import os

app = Flask(__name__)

LINE_TOKEN = os.getenv("LINE_TOKEN")
USER_ID = os.getenv("USER_ID")

@app.route("/mt4", methods=["POST"])
def mt4_notify():
    msg = request.form.get("msg", "")
    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": USER_ID,
        "messages": [{
            "type": "text",
            "text": msg
        }]
    }
    r = requests.post("https://api.line.me/v2/bot/message/push", json=payload, headers=headers)
    return "OK"
