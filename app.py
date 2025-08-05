import os
from flask import Flask, request
from dotenv import load_dotenv
from ingram_micro import quote_product, suggest_replacement

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "Ribbit AI Bot is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("data", {}).get("text", "").lower()
    print("Incoming message:", message)

    response = "🤖 I'm not sure what you need."

    if "quote" in message:
        sku = extract_sku(message)
        quantity = extract_quantity(message)
        if sku:
            response = quote_product(sku, quantity)
        else:
            response = "❓ Please include a SKU to get a quote."

    elif "replacement" in message:
        sku = extract_sku(message)
        if sku:
            response = suggest_replacement(sku)
        else:
            response = "❓ Please include a SKU to find replacements."

    return {"text": response}, 200

def extract_sku(text):
    words = text.upper().split()
    for word in words:
        if any(char.isdigit() for char in word) and len(word) > 4:
            return word
    return None

def extract_quantity(text):
    for word in text.split():
        if word.isdigit():
            return int(word)
    return 1

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)