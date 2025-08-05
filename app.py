from flask import Flask, request, jsonify
from webexteamssdk import WebexTeamsAPI
from openai import OpenAI
import os

app = Flask(__name__)
webex = WebexTeamsAPI(access_token=os.getenv("WEBEX_BOT_TOKEN"))
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message_id = data.get("data", {}).get("id")

    if not message_id:
        return jsonify({"error": "No message ID"}), 400

    message = webex.messages.get(message_id)
    user_message = message.text

    bot_id = webex.people.me().id
    user_message = user_message.replace(f"<@personId:{bot_id}>", "").strip()

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_message}]
    )

    gpt_response = response.choices[0].message.content

    webex.messages.create(roomId=message.roomId, text=gpt_response)
    return jsonify({"status": "ok"})