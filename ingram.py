def get_ingram_token():
    payload = {
        'client_id': os.environ['INGRAM_CLIENT_ID'],
        'client_secret': os.environ['INGRAM_CLIENT_SECRET'],
        'grant_type': 'client_credentials'
    }
    res = requests.post('https://api.ingrammicro.com/oauth/token', data=payload)
    
    if res.status_code != 200:
        print("Ingram Auth Error:", res.status_code, res.text)  # ⬅ Add this line

    return res.json().get('access_token')
