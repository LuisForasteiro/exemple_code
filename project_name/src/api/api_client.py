import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self):
        response = requests.get(f'{self.base_url}/data')
        return response.json()
