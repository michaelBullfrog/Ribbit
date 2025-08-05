from flask import Flask, request
from webexteamssdk import WebexTeamsAPI
from gpt import ask_chatgpt
from ingram import get_product_info
from zoho import create_quote
import os

app = Flask(__name__)
webex_api = WebexTeamsAPI(access_token=os.environ['WEBEX_BOT_ACCESS_TOKEN'])

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    msg_id = data['data']['id']
    msg = webex_api.messages.get(msg_id)

    if msg.personEmail.endswith('@webex.bot'):
        return "OK"

    user_query = msg.text.strip()
    gpt_response = ask_chatgpt(user_query)
    product_data = get_product_info(gpt_response)
    zoho_result = create_quote(product_data)

    webex_api.messages.create(roomId=msg.roomId, text=f"Quote created: {zoho_result}")
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
