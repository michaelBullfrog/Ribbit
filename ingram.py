# ingram.py
import requests
import os

def get_ingram_token():
    payload = {
        'client_id': os.environ['INGRAM_CLIENT_ID'],
        'client_secret': os.environ['INGRAM_CLIENT_SECRET'],
        'grant_type': 'client_credentials'
    }
    res = requests.post('https://api.ingrammicro.com/oauth/token', data=payload)

    if res.status_code != 200:
        print("Ingram Auth Error:", res.status_code, res.text)

    return res.json().get('access_token')  # safer than ['access_token']

def get_product_info(search_term):
    token = get_ingram_token()
    if not token:
        raise ValueError("Ingram token not retrieved — check credentials.")
    
    headers = {'Authorization': f'Bearer {token}'}
    params = {'keyword': search_term, 'limit': 1}
    res = requests.get('https://api.ingrammicro.com/products/v1/search', headers=headers, params=params)

    if res.status_code != 200:
        print("Product search failed:", res.status_code, res.text)
        return {}

    return res.json()
