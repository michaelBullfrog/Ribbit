import os
import requests

INGRAM_CLIENT_ID = os.getenv("INGRAM_CLIENT_ID")
INGRAM_CLIENT_SECRET = os.getenv("INGRAM_CLIENT_SECRET")
BASE_URL = "https://api.ingrammicro.com"

def get_access_token():
    url = f"{BASE_URL}/oauth/oauth30/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": INGRAM_CLIENT_ID,
        "client_secret": INGRAM_CLIENT_SECRET
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("access_token")

def search_sku(sku):
    token = get_access_token()
    url = f"{BASE_URL}/resellers/v6/catalog/skus/{sku}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def get_price_and_availability(sku, country_code="US"):
    token = get_access_token()
    url = f"{BASE_URL}/resellers/v6/catalog/priceandavailability"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    payload = {
        "items": [
            {"partNumber": sku}
        ],
        "sellingCountryCode": country_code
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def quote_product(sku, quantity):
    price_data = get_price_and_availability(sku)
    if not price_data:
        return "No price info found."

    item = price_data.get("items", [{}])[0]
    list_price = item.get("pricing", {}).get("listPrice", 0)
    availability = item.get("availability", {}).get("stockStatus", "Unknown")
    description = item.get("description", "No description")

    total_price = float(list_price) * quantity
    return f"🧾 Quote for {quantity} x {sku}:
- Description: {description}
- Unit Price: ${list_price:.2f}
- Total: ${total_price:.2f}
- Availability: {availability}"

def suggest_replacement(sku):
    # Placeholder — Ingram does not offer public EOL API replacements.
    # This should be customized if you have vendor-specific mappings.
    return f"🔁 No replacement data found for SKU {sku}. Please check vendor docs or support."