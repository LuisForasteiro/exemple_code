import requests

class AuthClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        response = requests.post(f'{self.base_url}/login', data={'username': username, 'password': password})
        return response.json()

    def refresh_token(self, refresh_token):
        response = requests.post(f'{self.base_url}/refresh', data={'refresh_token': refresh_token})
        return response.json()
