import requests
import os

def create_quote(product_data):
    headers = {'Authorization': f'Zoho-oauthtoken {os.environ["ZOHO_ACCESS_TOKEN"]}'}
    payload = {
        "data": [
            {
                "Product_Name": product_data["products"][0]["name"],
                "Quantity": 1,
                "Rate": product_data["products"][0]["price"],
                "Description": product_data["products"][0]["description"]
            }
        ]
    }
    res = requests.post('https://www.zohoapis.com/crm/v2/Quotes', headers=headers, json=payload)
    return res.json()
