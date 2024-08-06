import requests

class DataFetcher:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint):
        response = requests.get(f'{self.base_url}/{endpoint}')
        return response.json()
