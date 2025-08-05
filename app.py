import os
import json
from flask import Flask, request
from webexteamssdk import WebexTeamsAPI
import openai

# Load environment variables
webex_token = os.getenv("WEBEX_BOT_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

print("WEBEX_BOT_TOKEN:", webex_token[:10] if webex_token else "NOT FOUND")  # Debug
print("OPENAI_API_KEY:", openai.api_key[:10] if openai.api_key else "NOT FOUND")  # Debug

# Init SDKs
webex = WebexTeamsAPI(access_token=webex_token)
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received data:", json.dumps(data, indent=2))  # Debug

    if "data" in data:
        message_id = data["data"]["id"]
        room_id = data["data"]["roomId"]

        # Avoid responding to the bot's own messages
        message = webex.messages.get(message_id)
        if message.personEmail == webex.people.me().emails[0]:
            return "Ignored", 200

        prompt = message.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for Webex users."},
                {"role": "user", "content": prompt}
            ]
        )

        answer = response["choices"][0]["message"]["content"]
        webex.messages.create(roomId=room_id, text=answer)
        return "OK", 200

    return "No data", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
