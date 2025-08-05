import os
from flask import Flask, request
from dotenv import load_dotenv
from ingram_micro import quote_product, suggest_replacement

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return "Ribbit bot is live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if "data" in data:
        # Webex message handling logic
        print("Webhook received:", data)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
