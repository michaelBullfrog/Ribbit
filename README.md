# Webex ChatGPT Bot (Clean Version)

This bot listens to messages in Webex where it's mentioned and replies using OpenAI's ChatGPT.

## Setup

1. Create `.env` with your tokens:
```
WEBEX_BOT_TOKEN=your_webex_token
OPENAI_API_KEY=your_openai_key
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run:
```
python app.py
```

4. Set webhook to `/webhook` endpoint on your Render or server.