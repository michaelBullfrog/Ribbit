# Webex Ingram Quote Bot

This is a Webex chatbot powered by ChatGPT that integrates with Ingram Micro's product catalog and Zoho CRM to generate quotes in real time.

## Features
- Natural language understanding via GPT-4
- Product search from Ingram Micro APIs
- Quote creation in Zoho CRM
- Webex Bot integration

## Setup
1. Clone this repo
2. Create a `.env` file with the following:

```env
WEBEX_BOT_ACCESS_TOKEN=your_webex_token
OPENAI_API_KEY=your_openai_key
INGRAM_CLIENT_ID=your_ingram_id
INGRAM_CLIENT_SECRET=your_ingram_secret
ZOHO_ACCESS_TOKEN=your_zoho_token
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask app:
```bash
python app.py
```

## Deployment

### Render.com Steps:
1. Create a new Web Service
2. Connect your GitHub repo or upload the zip and choose `Flask` for environment
3. Set environment variables in the Render dashboard
4. Set the start command to:
```bash
python app.py
```
5. Expose the webhook URL (e.g., `https://yourservice.onrender.com/webhook`) in your Webex Bot configuration

---
MIT License
