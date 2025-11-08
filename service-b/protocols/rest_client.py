# clients/rest_client.py
import requests

class RESTClientService:
    # Class constructor
    def __init__(self, base_url):
        self.base_url = base_url

    # Example function to get a users from service-a
    def get_users(self):
        url = f"{self.base_url}/users"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    # Check if service A is reachable
    def ping_server(self):
        url = f"{self.base_url}/ping"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()