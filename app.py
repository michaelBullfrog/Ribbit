
import os
import sys
from flask import Flask, request
import openai
from webexteamssdk import WebexTeamsAPI

print("Starting app.py...")
print("WEBEX_BOT_TOKEN:", os.getenv("WEBEX_BOT_TOKEN")[:10] if os.getenv("WEBEX_BOT_TOKEN") else "NOT SET")
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY")[:10] if os.getenv("OPENAI_API_KEY") else "NOT SET")

app = Flask(__name__)

webex = WebexTeamsAPI(access_token=os.getenv("WEBEX_BOT_TOKEN"))
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    print("Webhook hit.")
    data = request.json
    print("Payload received:", data)
    return "OK", 200

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="0.0.0.0", port=10000)
