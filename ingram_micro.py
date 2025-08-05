# ingram_micro.py
import os
import requests

def quote_product(sku, quantity):
    client_id = os.getenv("INGRAM_CLIENT_ID")
    client_secret = os.getenv("INGRAM_CLIENT_SECRET")

    # Get access token
    auth_response = requests.post(
        "https://api.ingrammicro.com/oauth/oauth20/token",
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }
    )

    if auth_response.status_code != 200:
        return "❌ Failed to authenticate with Ingram Micro."

    token = auth_response.json().get("access_token")

    # Call product quote API (this endpoint may differ based on access)
    headers = {"Authorization": f"Bearer {token}"}
    quote_response = requests.get(
        f"https://api.ingrammicro.com/products/v1/sku/{sku}",
        headers=headers
    )

    if quote_response.status_code != 200:
        return f"❌ Could not retrieve quote for SKU: {sku}"

    product_data = quote_response.json()
    name = product_data.get("name", "Unknown Product")
    price = product_data.get("price", {}).get("list", "N/A")

    return f"💡 {name} (SKU: {sku})\nPrice: {price} x {quantity}"

def suggest_replacement(sku):
    # Simulated logic — Ingram may provide EOL/replacement APIs
    return f"🔄 Suggested replacement for {sku}: Not available via API yet."
