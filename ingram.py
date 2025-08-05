import requests
import os

def get_ingram_token():
    payload = {
        'client_id': os.environ['INGRAM_CLIENT_ID'],
        'client_secret': os.environ['INGRAM_CLIENT_SECRET'],
        'grant_type': 'client_credentials'
    }
    res = requests.post('https://api.ingrammicro.com/oauth/token', data=payload)
    return res.json()['access_token']

def get_product_info(search_term):
    token = get_ingram_token()
    headers = {'Authorization': f'Bearer {token}'}
    params = {'keyword': search_term, 'limit': 1}
    res = requests.get('https://api.ingrammicro.com/products/v1/search', headers=headers, params=params)
    return res.json()
