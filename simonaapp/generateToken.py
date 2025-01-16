import requests
from django.http import JsonResponse

def get_access_token(request):
    consumer_key = "HZwq7G5DoJVdPcFPZedLjga7ILTal6HjkqcXXFmGbjoD59Ai"
    consumer_secret = "GzJB6LUkw79F3cJwyISiGGawNIL2KGKKFoHP5IzLM8p4nbhKQuNNGYtKGQ6h6zid"
    access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    headers = {'Content-Type': 'application/json'}
    auth = (consumer_key, consumer_secret)
    try:
        response = requests.get(access_token_url, headers=headers, auth=auth)
        response.raise_for_status()
        result = response.json()
        access_token = result['access_token']
        return JsonResponse({'access_token':access_token})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error':str(e)})