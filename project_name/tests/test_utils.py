import unittest
from src.utils.json_utils import load_json, save_json
import os

class TestJSONUtils(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test.json'
        self.data = {'key': 'value'}

    def test_save_json(self):
        save_json(self.data, self.file_path)
        self.assertTrue(os.path.exists(self.file_path))
    
    def test_load_json(self):
        save_json(self.data, self.file_path)
        loaded_data = load_json(self.file_path)
        self.assertEqual(loaded_data, self.data)
    
    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

if __name__ == '__main__':
    unittest.main()
