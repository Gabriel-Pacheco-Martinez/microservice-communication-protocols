# clients/graphql_client.py
import requests

class GraphQLClientService:
    def __init__(self, base_url):
        self.base_url = base_url

    # ====
    # Send a GraphQL query or mutation
    def execute(self, query: str, variables: dict = None):
        payload = {"query": query, "variables": variables or {}}
        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()

        data = response.json()
        if "errors" in data:
            raise Exception(f"GraphQL Error: {data['errors']}")
        return data["data"]

    # ====
    # Fetch all users
    def get_users(self):
        query = """
        query {
            users {
                id
                name
                email
            }
        }
        """
        result = self.execute(query)
        return result["users"]

    # ====
    # Add a user
    def add_user(self, name: str, email: str):
        mutation = """
        mutation($name: String!, $email: String!) {
            addUser(name: $name, email: $email) {
                id
                name
                email
            }
        }
        """
        variables = {"name": name, "email": email}
        result = self.execute(mutation, variables)
        return result["addUser"]