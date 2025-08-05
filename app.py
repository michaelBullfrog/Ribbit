from flask import Flask, request
import requests
import openai
import os

app = Flask(__name__)

WEBEX_BOT_TOKEN = os.getenv("WEBEX_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def get_bot_person_id():
    url = "https://webexapis.com/v1/people/me"
    headers = {"Authorization": f"Bearer {WEBEX_BOT_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json().get("id")

BOT_PERSON_ID = get_bot_person_id()

def get_message_text_and_room(message_id):
    url = f"https://webexapis.com/v1/messages/{message_id}"
    headers = {"Authorization": f"Bearer {WEBEX_BOT_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get("text", ""), data.get("roomId", "")

def send_webex_message(room_id, text):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"roomId": room_id, "text": text}
    requests.post(url, headers=headers, json=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if not data or "data" not in data:
        return "Invalid request", 400

    message_id = data["data"]["id"]
    sender_id = data["data"]["personId"]

    if sender_id == BOT_PERSON_ID:
        return "Ignoring bot's own message", 200

    message_text, room_id = get_message_text_and_room(message_id)
    if not message_text:
        return "No message content", 200

    if message_text.startswith("@") or message_text.startswith("<@"):
        parts = message_text.split(" ", 1)
        user_input = parts[1] if len(parts) > 1 else ""
    else:
        user_input = message_text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        ai_reply = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        ai_reply = f"Error: {str(e)}"

    send_webex_message(room_id, ai_reply)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)