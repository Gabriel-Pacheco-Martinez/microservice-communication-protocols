# clients/graphql_client.py
import requests

class GraphQLClientService:
    # Class constructor
    def __init__(self, base_url):
        self.base_url = base_url

    # Get all users
    def get_users(self):
        query = """
        query {
            getUsers {
                id
                name
                email
            }
        }
        """
        response = requests.post(self.base_url, json={"query": query})
        response.raise_for_status()
        data = response.json()
        return data["data"]["getUsers"]

    # Add a new user
    def add_user(self, payload):
        name = payload.get("name")
        email = payload.get("email")
        mutation = f"""
        mutation {{
            addUser(name: "{name}", email: "{email}") {{
                id
                name
                email
            }}
        }}
        """
        response = requests.post(self.base_url, json={"query": mutation})
        response.raise_for_status()
        data = response.json()
        return data["data"]["addUser"]