import requests

class FileUploader:
    def __init__(self, base_url):
        self.base_url = base_url

    def upload_file(self, file_path):
        with open(file_path, 'rb') as file:
            response = requests.post(f'{self.base_url}/upload', files={'file': file})
        return response.json()
