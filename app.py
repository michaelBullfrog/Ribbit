from flask import Flask, request
from webexteamssdk import WebexTeamsAPI
from dotenv import load_dotenv
import os
from gpt import ask_chatgpt

load_dotenv()
app = Flask(__name__)

WEBEX_BOT_TOKEN = os.environ["WEBEX_BOT_TOKEN"]
api = WebexTeamsAPI(access_token=WEBEX_BOT_TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data["resource"] == "messages" and data["event"] == "created":
        message_id = data["data"]["id"]
        message = api.messages.get(message_id)
        sender = message.personEmail

        me = api.people.me()
        if sender == me.emails[0]:
            return "OK", 200

        prompt = message.text.replace(me.displayName, "").strip()
        response = ask_chatgpt(prompt)

        api.messages.create(roomId=message.roomId, text=response)

    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Webex ChatGPT Bot is live!"
