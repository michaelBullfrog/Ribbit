import os
from dotenv import load_dotenv
load_dotenv()

WEBEX_BOT_ACCESS_TOKEN = os.getenv("WEBEX_BOT_ACCESS_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INGRAM_CLIENT_ID = os.getenv("INGRAM_CLIENT_ID")
INGRAM_CLIENT_SECRET = os.getenv("INGRAM_CLIENT_SECRET")
ZOHO_ACCESS_TOKEN = os.getenv("ZOHO_ACCESS_TOKEN")
