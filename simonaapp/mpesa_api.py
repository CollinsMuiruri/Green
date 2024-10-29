import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth


def generate_access_token():
    """Generates an OAuth access token for Safaricom M-PESA API"""
    url = f"{settings.SAFARICOM_API_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=HTTPBasicAuth(settings.SAFARICOM_CONSUMER_KEY, settings.SAFARICOM_CONSUMER_SECRET))
    
    if response.status_code == 200:
        try:
            return response.json().get('access_token')
        except ValueError:
            print("Error parsing JSON response:", response.text)
            return None
    else:
        print(f"Failed to generate access token. Status Code: {response.status_code}")
        print("Response Text:", response.text)
        return None


def register_url():
    """Registers the callback URLs with the M-PESA API"""
    access_token = generate_access_token()
    if not access_token:
        print("Failed to retrieve access token.")
        return None  # Exit if token generation failed

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "ShortCode": settings.SAFARICOM_SHORTCODE,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://green-wv6k.onrender.com/api/mpesa/confirmation",
        "ValidationURL": "https://green-wv6k.onrender.com/api/mpesa/validation"
    }
    
    response = requests.post(settings.SAFARICOM_REGISTER_URL_API, headers=headers, json=payload)
    
    # Check if the response is OK before trying to parse JSON
    if response.status_code == 200:
        return response.json()  # Success case
    else:
        # Print the response for debugging
        print(f"Error registering URL: Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return None  # Or handle as needed
