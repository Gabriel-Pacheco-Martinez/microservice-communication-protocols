# clients/rest_client.py
import requests

class RESTClientService:
    # Class constructor
    def __init__(self, base_url):
        self.base_url = base_url

    # Get all users
    def get_users(self):
        url = f"{self.base_url}/api/users"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    # Add a user
    def add_user(self, payload):
        url = f"{self.base_url}/api/users"
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    # Check if service A is reachable
    def ping_server(self):
        url = f"{self.base_url}/api/ping"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()